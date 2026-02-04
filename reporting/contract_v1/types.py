from __future__ import annotations

from typing import Literal, Optional, TypedDict, Union

FieldStatus = Literal["computed", "not_computed", "not_applicable", "hidden"]


class FieldString(TypedDict):
    value: Optional[str]
    status: FieldStatus


class FieldNumber(TypedDict):
    value: Optional[Union[float, str]]
    status: FieldStatus


class FieldBool(TypedDict):
    value: Optional[bool]
    status: FieldStatus


class SectionVisibility(TypedDict):
    visible: bool
    reason: str


class AnalysisStatus(TypedDict):
    computed: bool
    as_of: str


class LayoutSpec(TypedDict):
    top_banner_mode: Literal["client_and_analyst", "analyst_only"]
    center_key_data: bool


class Underlying(TypedDict):
    ticker: FieldString
    name: FieldString
    sector: FieldString
    spot: FieldNumber
    move_pct: FieldNumber
    dividend_yield: FieldNumber
    high_52w: FieldNumber
    low_52w: FieldNumber
    earnings_date: FieldString


class Analyst(TypedDict):
    ubs_rating: FieldString
    price_target: FieldNumber
    cio_view: FieldString


class ClientPosition(TypedDict):
    shares: FieldNumber
    avg_cost: FieldNumber
    market_value: FieldNumber
    pnl_dollar: FieldNumber
    pnl_percent: FieldNumber


class Strategy(TypedDict):
    name: FieldString
    description: FieldString


class Leg(TypedDict):
    action: FieldString
    type: FieldString
    quantity: FieldNumber
    expiry: FieldString
    strike: FieldNumber
    price: FieldNumber
    delta: FieldNumber
    otm_percent: FieldNumber
    premium: FieldNumber


class Metrics(TypedDict):
    max_profit: FieldNumber
    max_loss: FieldNumber
    reward_risk: FieldNumber
    max_roi: FieldNumber
    min_roi: FieldNumber
    capital_basis: FieldNumber
    net_cost: FieldNumber
    net_premium_total: FieldNumber
    net_premium_per_share: FieldNumber
    yield_percent: FieldNumber


class Scenario(TypedDict, total=False):
    label: FieldString
    narrative: FieldString
    underlying_price: FieldNumber
    move_pct: FieldNumber
    stock_pnl: FieldNumber
    option_pnl: FieldNumber
    option_roi: FieldNumber
    net_pnl: FieldNumber
    net_roi: FieldNumber


class KeyLevelRow(TypedDict):
    label: FieldString
    underlying_price: FieldNumber
    move_pct: FieldNumber
    stock_pnl: FieldNumber
    option_pnl: FieldNumber
    option_roi: FieldNumber
    net_pnl: FieldNumber
    net_roi: FieldNumber


class Sections(TypedDict):
    client_position: SectionVisibility
    analyst_view: SectionVisibility
    key_data: SectionVisibility
    scenario_analysis: SectionVisibility
    key_levels: SectionVisibility
    disclosures: SectionVisibility


class ReportContractV1(TypedDict):
    meta: dict
    analysis_status: AnalysisStatus
    layout: LayoutSpec
    sections: Sections
    underlying: Underlying
    analyst: Analyst
    client_position: ClientPosition
    strategy: Strategy
    legs: list[Leg]
    metrics: Metrics
    scenarios: list[Scenario]
    key_levels: dict
    disclosures: dict
