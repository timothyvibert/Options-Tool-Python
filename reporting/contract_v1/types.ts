export type FieldStatus =
  | "computed"
  | "not_computed"
  | "not_applicable"
  | "hidden";

export type Field<T> = {
  value: T | null;
  status: FieldStatus;
};

export type FieldString = Field<string>;
export type FieldNumber = Field<number | string>;
export type FieldBool = Field<boolean>;

export type SectionVisibility = {
  visible: boolean;
  reason: string;
};

export type LayoutSpec = {
  top_banner_mode: "client_and_analyst" | "analyst_only";
  center_key_data: boolean;
};

export type AnalysisStatus = {
  computed: boolean;
  as_of: string;
};

export type Underlying = {
  ticker: FieldString;
  name: FieldString;
  sector: FieldString;
  spot: FieldNumber;
  move_pct: FieldNumber;
  dividend_yield: FieldNumber;
  high_52w: FieldNumber;
  low_52w: FieldNumber;
  earnings_date: FieldString;
};

export type Analyst = {
  ubs_rating: FieldString;
  price_target: FieldNumber;
  cio_view: FieldString;
};

export type ClientPosition = {
  shares: FieldNumber;
  avg_cost: FieldNumber;
  market_value: FieldNumber;
  pnl_dollar: FieldNumber;
  pnl_percent: FieldNumber;
};

export type Strategy = {
  name: FieldString;
  description: FieldString;
};

export type Leg = {
  action: FieldString;
  type: FieldString;
  quantity: FieldNumber;
  expiry: FieldString;
  strike: FieldNumber;
  price: FieldNumber;
  delta: FieldNumber;
  otm_percent: FieldNumber;
  premium: FieldNumber;
};

export type Metrics = {
  max_profit: FieldNumber;
  max_loss: FieldNumber;
  reward_risk: FieldNumber;
  max_roi: FieldNumber;
  min_roi: FieldNumber;
  capital_basis: FieldNumber;
  net_cost: FieldNumber;
  net_premium_total: FieldNumber;
  net_premium_per_share: FieldNumber;
  yield_percent: FieldNumber;
};

export type Scenario = {
  label: FieldString;
  narrative?: FieldString;
  underlying_price: FieldNumber;
  move_pct: FieldNumber;
  stock_pnl: FieldNumber;
  option_pnl: FieldNumber;
  option_roi: FieldNumber;
  net_pnl: FieldNumber;
  net_roi: FieldNumber;
};

export type KeyLevelRow = {
  label: FieldString;
  underlying_price: FieldNumber;
  move_pct: FieldNumber;
  stock_pnl: FieldNumber;
  option_pnl: FieldNumber;
  option_roi: FieldNumber;
  net_pnl: FieldNumber;
  net_roi: FieldNumber;
};

export type Sections = {
  client_position: SectionVisibility;
  analyst_view: SectionVisibility;
  key_data: SectionVisibility;
  scenario_analysis: SectionVisibility;
  key_levels: SectionVisibility;
  disclosures: SectionVisibility;
};

export type ReportContractV1 = {
  meta: { report_version: "v1" };
  analysis_status: AnalysisStatus;
  layout: LayoutSpec;
  sections: Sections;
  underlying: Underlying;
  analyst: Analyst;
  client_position: ClientPosition;
  strategy: Strategy;
  legs: Leg[];
  metrics: Metrics;
  scenarios: Scenario[];
  key_levels: { rows: KeyLevelRow[] };
  disclosures: { text: FieldString };
};
