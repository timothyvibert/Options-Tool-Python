type AnyRecord = Record<string, any>;

const MISSING = "--";

const toText = (value: any, fallback = MISSING): string => {
  if (value === null || value === undefined) return fallback;
  if (typeof value === "string" && value.trim() === "") return fallback;
  return String(value);
};

const toNumber = (value: any): number | null => {
  if (value === null || value === undefined) return null;
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (typeof value === "string") {
    const trimmed = value.trim();
    if (!trimmed || trimmed === MISSING) return null;
    const negative = trimmed.startsWith("(") && trimmed.endsWith(")");
    const cleaned = trimmed.replace(/[(),$%]/g, "");
    const parsed = Number.parseFloat(cleaned);
    if (Number.isFinite(parsed)) {
      return negative ? -parsed : parsed;
    }
  }
  return null;
};

const toPercentRatio = (value: any): number | string => {
  if (typeof value === "string" && value.includes("%")) {
    const parsed = toNumber(value);
    if (parsed !== null) return parsed / 100.0;
  }
  if (typeof value === "number") return value;
  return value ?? MISSING;
};

const toNumberOrText = (value: any): number | string => {
  const num = toNumber(value);
  if (num === null) return toText(value);
  return num;
};

const pick = (obj: AnyRecord | null | undefined, keys: string[]): any => {
  if (!obj) return undefined;
  for (const key of keys) {
    if (key in obj) return obj[key];
  }
  return undefined;
};

const normalizeSide = (raw: string): { action: string; type: string } => {
  const text = raw.toLowerCase();
  const type = text.includes("put") ? "Put" : text.includes("call") ? "Call" : "";
  const action = text.includes("short") || text.includes("sell") ? "Sell" : "Buy";
  return { action, type };
};

const buildMetrics = (rows: any[]) => {
  const byMetric = new Map<string, AnyRecord>();
  for (const row of rows) {
    if (row && typeof row.metric === "string") {
      byMetric.set(row.metric, row);
    }
  }
  const metricValue = (label: string, field: "options" | "combined") => {
    const row = byMetric.get(label);
    if (!row) return 0;
    if (label.includes("ROI") || label.includes("Prem %")) {
      return toPercentRatio(row[field]);
    }
    return toNumberOrText(row[field]);
  };

  return {
    maxProfit: {
      options: metricValue("Max Profit", "options"),
      combined: metricValue("Max Profit", "combined"),
    },
    maxLoss: {
      options: metricValue("Max Loss", "options"),
      combined: metricValue("Max Loss", "combined"),
    },
    capitalBasis: {
      options: metricValue("Capital Basis", "options"),
      combined: metricValue("Capital Basis", "combined"),
    },
    maxROI: {
      options: metricValue("Max ROI", "options"),
      combined: metricValue("Max ROI", "combined"),
    },
    minROI: {
      options: metricValue("Min ROI", "options"),
      combined: metricValue("Min ROI", "combined"),
    },
    rewardRisk: {
      options: metricValue("Reward/Risk", "options"),
      combined: metricValue("Reward/Risk", "combined"),
    },
    costCredit: {
      options: metricValue("Cost/Credit", "options"),
      combined: metricValue("Cost/Credit", "combined"),
    },
    notionalExp: {
      options: metricValue("Notional Exposure", "options"),
      combined: metricValue("Notional Exposure", "combined"),
    },
    netPremPerShare: {
      options: metricValue("Net Prem/Share", "options"),
      combined: metricValue("Net Prem/Share", "combined"),
    },
    netPremPercent: {
      options: metricValue("Net Prem % Spot", "options"),
      combined: metricValue("Net Prem % Spot", "combined"),
    },
  };
};

export const mapReportContractToTemplateData = (contract: AnyRecord) => {
  const header = (contract?.header as AnyRecord) || {};
  const structure = (contract?.structure as AnyRecord) || {};
  const metricsRows = Array.isArray(contract?.metrics?.rows)
    ? contract.metrics.rows
    : [];
  const keyLevelsRows = Array.isArray(contract?.key_levels_display_rows_by_price)
    ? contract.key_levels_display_rows_by_price
    : [];
  const scenarioCards = Array.isArray(contract?.scenario_analysis_cards)
    ? contract.scenario_analysis_cards
    : [];

  const lastPrice = toNumber(header.last_price) ?? 0;
  const shares = toNumber(header.shares) ?? 0;
  const avgCost = toNumber(header.avg_cost) ?? 0;
  const mktValue = lastPrice * shares;
  const costValue = avgCost * shares;
  const pnlDollar = mktValue - costValue;
  const pnlPercent = costValue !== 0 ? (pnlDollar / costValue) * 100 : 0;

  const optionLegs = Array.isArray(structure.legs)
    ? structure.legs.map((leg: AnyRecord, index: number) => {
        const sideText = toText(leg.side);
        const sideInfo = normalizeSide(sideText);
        return {
          leg: toNumber(leg.leg) ?? index + 1,
          action: sideInfo.action,
          quantity: 1,
          expiration: toText(leg.Expiry || leg.expiry),
          strike: toNumber(leg.strike) ?? 0,
          type: sideInfo.type || toText(leg.type || leg.kind),
          price: Math.abs(toNumber(leg.premium) ?? 0),
          delta: 0,
          otmPercent: "--",
          premium: toNumber(leg.premium) ?? 0,
        };
      })
    : [];

  const netPremium = toNumber(structure.net_premium_total) ?? 0;
  const metrics = buildMetrics(metricsRows);

  const keyLevels = keyLevelsRows.map((row: AnyRecord) => ({
    scenario: toText(row["Scenario"] ?? row.scenario),
    price: toNumberOrText(row["Price"] ?? row.price),
    movePercent: toText(row["Move %"] ?? row.move_pct ?? row.movePercent),
    stockPnL: toNumberOrText(row["Stock PnL"] ?? row.stock_pnl ?? row.stockPnL),
    optionPnL: toNumberOrText(row["Option PnL"] ?? row.option_pnl ?? row.optionPnL),
    optionROI: toText(row["Option ROI"] ?? row.option_roi ?? row.optionROI),
    netPnL: toNumberOrText(row["Net PnL"] ?? row.net_pnl ?? row.netPnL),
    netROI: toText(row["Net ROI"] ?? row.net_roi ?? row.netROI),
  }));

  const scenarioAnalysis = scenarioCards.map((card: AnyRecord) => {
    const title = toText(card.title);
    const typeText = title.toLowerCase();
    const type = typeText.includes("bear")
      ? "bearish"
      : typeText.includes("bull")
      ? "bullish"
      : "stagnant";
    return {
      title,
      condition: toText(card.condition),
      description: toText(card.body ?? card.description),
      type,
    };
  });

  const reportData = {
    date: toText(header.report_time),
    strategyName: toText(header.strategy_name),
    stockDetails: {
      ticker: toText(header.ticker),
      name: toText(header.name),
      sector: toText(header.sector),
      ubsGrpRating: "N/A",
      ubsGrpTarget: 0,
      ubsCioRating: "N/A",
      lastPrice,
      tenDayChange: "0.00%",
      fiftyTwoWeekHigh: toNumber(header.high_52w) ?? 0,
      fiftyTwoWeekLow: toNumber(header.low_52w) ?? 0,
      dividendYield: toNumber(header.dividend_yield) ?? 0,
      earningsDate: toText(header.earnings_date),
    },
    clientPosition: shares
      ? {
          shares,
          avgCost,
          mktValue,
          costValue,
          pnlDollar,
          pnlPercent: Number.isFinite(pnlPercent)
            ? Number(pnlPercent.toFixed(2))
            : 0,
        }
      : null,
    strategyDescription: toText(contract?.strategy_description ?? ""),
    optionLegs,
    netPremium,
    metrics,
    keyLevels,
    scenarioAnalysis,
    keyLevelsCommentary: [],
  };

  return reportData;
};
