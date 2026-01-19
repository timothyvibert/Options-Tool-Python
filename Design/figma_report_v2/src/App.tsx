import { StrategyReport } from "./components/StrategyReport";

export default function App() {
  // Sample data - in production, this would come from your Python/Streamlit backend
  const reportData = {
    date: "1/7/2026",
    strategyName: "Rev Iron Condor",
    stockDetails: {
      ticker: "AMZN US Equity",
      name: "Amazon.com Inc",
      sector: "Consumer Discretionary",
      ubsGrpRating: "buy",
      ubsGrpTarget: 310.00,
      ubsCioRating: "N/A",
      lastPrice: 240.93,
      tenDayChange: "0.00%",
      fiftyTwoWeekHigh: 258.60,
      fiftyTwoWeekLow: 161.38,
      dividendYield: 0.00,
      earningsDate: "2/6/2026"
    },
    clientPosition: {
      shares: 100,
      avgCost: 198.00,
      mktValue: 24093.00,
      costValue: 19800.00,
      pnlDollar: 4293.00,
      pnlPercent: 21.68
    },
    strategyDescription: "A reverse iron condor consists of buying a bull call spread and buying a bear put spread. It profits from high volatility, gaining value if the stock moves outside the inner strikes.",
    optionLegs: [
      { leg: 1, action: "Sell", quantity: 1, expiration: "September 19, 2026", strike: 210, type: "Put", price: 11.90, delta: -0.25, otmPercent: "12.64%", premium: 1190.00 },
      { leg: 2, action: "Buy", quantity: 1, expiration: "September 18, 2026", strike: 230, type: "Put", price: 19.30, delta: -0.36, otmPercent: "4.54%", premium: -1930.00 },
      { leg: 3, action: "Buy", quantity: 1, expiration: "September 18, 2026", strike: 250, type: "Call", price: 26.20, delta: 0.54, otmPercent: "3.76%", premium: -2620.00 },
      { leg: 4, action: "Sell", quantity: 1, expiration: "September 18, 2026", strike: 270, type: "Call", price: 18.20, delta: 0.43, otmPercent: "12.07%", premium: 1820.00 }
    ],
    netPremium: -1540.00,
    metrics: {
      maxProfit: { options: 2707.00, combined: "Unlimited" },
      maxLoss: { options: -7293.00, combined: -67293.00 },
      capitalBasis: { options: 7293.00, combined: 67293.00 },
      maxROI: { options: 0.37, combined: "Unlimited" },
      minROI: { options: -1.00, combined: -1.00 },
      rewardRisk: { options: 0.37, combined: "N/A" },
      costCredit: { options: -2707.00, combined: 67293.00 },
      notionalExp: { options: 275088.00, combined: 343680.00 },
      netPremPerShare: { options: -27.07, combined: -27.07 },
      netPremPercent: { options: -0.04, combined: -0.04 }
    },
    keyLevels: [
      {
        scenario: "Stock to Zero",
        price: "---",
        movePercent: "-100.00%",
        stockPnL: -19800,
        optionPnL: 460,
        optionROI: "29.87%",
        netPnL: -19340,
        netROI: "-90.63%"
      },
      {
        scenario: "Combined Breakeven 1",
        price: 193.40,
        movePercent: "-19.73%",
        stockPnL: -460,
        optionPnL: 460,
        optionROI: "29.87%",
        netPnL: 0,
        netROI: "0.00%"
      },
      {
        scenario: "Stock Cost Basis",
        price: 198.00,
        movePercent: "-17.82%",
        stockPnL: 0,
        optionPnL: 460,
        optionROI: "29.87%",
        netPnL: 460,
        netROI: "2.16%"
      },
      {
        scenario: "Strike Level 1",
        price: 210.00,
        movePercent: "-12.84%",
        stockPnL: 1200,
        optionPnL: 460,
        optionROI: "29.87%",
        netPnL: 1660,
        netROI: "7.78%"
      },
      {
        scenario: "Strike Level 2",
        price: 230.00,
        movePercent: "-4.54%",
        stockPnL: 3200,
        optionPnL: -1540,
        optionROI: "-100.00%",
        netPnL: 1660,
        netROI: "7.78%"
      },
      {
        scenario: "Current Market Price",
        price: 240.93,
        movePercent: "0.00%",
        stockPnL: 4293,
        optionPnL: -1540,
        optionROI: "-100.00%",
        netPnL: 2753,
        netROI: "12.90%"
      },
      {
        scenario: "Strike Level 3",
        price: 250.00,
        movePercent: "3.76%",
        stockPnL: 5200,
        optionPnL: -1540,
        optionROI: "-100.00%",
        netPnL: 3660,
        netROI: "17.15%"
      },
      {
        scenario: "Strike Level 4",
        price: 270.00,
        movePercent: "12.07%",
        stockPnL: 7200,
        optionPnL: 460,
        optionROI: "29.87%",
        netPnL: 7660,
        netROI: "35.90%"
      },
      {
        scenario: "Stock to Infinity",
        price: "∞",
        movePercent: "---",
        stockPnL: "∞",
        optionPnL: 460,
        optionROI: "29.87%",
        netPnL: "Unlimited",
        netROI: "Unlimited"
      }
    ],
    scenarioAnalysis: [
      {
        title: "Bearish Case",
        condition: "If Stock falls to $210 - $230",
        description: "The \"Bear Put Spread\" kicks in. The options strategy gains value, offsetting some losses from the stock holding. This is your \"Protection Zone\".",
        type: "bearish"
      },
      {
        title: "Stagnant Case",
        condition: "If Stock stays $230 - $250",
        description: "The \"Premium Decay Zone\". The stock isn't moving enough to trigger the Call spread, and hasn't fallen enough to need the Put spread. The $1,540 cost acts as a drag on performance.",
        type: "stagnant"
      },
      {
        title: "Bullish Case",
        condition: "If Stock Rallies > $270",
        description: "Upside is uncapped. The stock appreciates, and the Call Spread (250/270) adds additional profit, enhancing the total return beyond just holding the stock alone.",
        type: "bullish"
      }
    ],
    keyLevelsCommentary: [
      {
        level: "Stock to Zero",
        commentary: "Big-move zone: A larger move outside ($230.00-$250.00) is typically what this structure needs to improve. Stock + Options (combined): The option overlay is offsetting part of the stock decline. Most of the movement here is coming from the stock position."
      },
      {
        level: "Combined Breakeven 1",
        commentary: "Combined Breakeven: Net position turns profitable above $193.40."
      },
      {
        level: "Stock Cost Basis",
        commentary: "Big-move zone: A larger move outside ($230.00-$250.00) is typically what this structure needs to improve. Stock + Options (combined): Most of the movement here is coming from the option overlay."
      },
      {
        level: "Strike Level 1",
        commentary: "Big-move zone: A larger move outside ($230.00-$250.00) is typically what this structure needs to improve. Stock + Options (combined): Both the stock and the option overlay are helping at this level. Most of the movement here is coming from the stock position."
      },
      {
        level: "Strike Level 2",
        commentary: "Premium-decay zone: If the stock stays inside the central range, the position can lose value over time. Stock + Options (combined): The option overlay is giving back part of the stock gains (the trade-off for premium/structure). Most of the movement here is coming from the stock position."
      },
      {
        level: "Current Market Price",
        commentary: "Current Status: Position is profitable. Strategy is lagging stock holding by $1,540 (drag)."
      },
      {
        level: "Strike Level 3",
        commentary: "Premium-decay zone: If the stock stays inside the central range, the position can lose value over time. Stock + Options (combined): The option overlay is giving back part of the stock gains (the trade-off for premium/structure). Most of the movement here is coming from the stock position."
      },
      {
        level: "Strike Level 4",
        commentary: "Big-move zone: A larger move outside ($230.00-$250.00) is typically what this structure needs to improve. Stock + Options (combined): Both the stock and the option overlay are helping at this level. Most of the movement here is coming from the stock position."
      },
      {
        level: "Stock to Infinity",
        commentary: "Big-move zone: A larger move outside ($230.00-$250.00) is typically what this structure needs to improve. Stock + Options (combined): Upside is not capped; gains can continue to grow as the stock rises."
      }
    ]
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <StrategyReport data={reportData} />
    </div>
  );
}
