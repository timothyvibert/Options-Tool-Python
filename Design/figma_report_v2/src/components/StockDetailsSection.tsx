import { TrendingUp, TrendingDown, Activity, Target, Building2, Calendar, PieChart } from "lucide-react";

interface StockDetailsSectionProps {
  stockDetails: any;
  clientPosition: any;
}

export function StockDetailsSection({ stockDetails, clientPosition }: StockDetailsSectionProps) {
  return (
    <div className="mb-4">
      <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden flex divide-x divide-gray-100 min-h-[100px]">
          
        {/* Section 1: Stock Profile (Flex-1.5) */}
        <div className="flex-[1.5] p-3 flex flex-col justify-between">
          <div>
            {/* Company Name - INCREASED SIZE */}
            <h3 className="text-lg font-bold text-gray-900 leading-none mb-1.5">{stockDetails.name}</h3>
            
            {/* Price & Change Row - REDUCED PRICE SIZE */}
            <div className="flex items-baseline gap-2 mb-1">
              <span className="text-base font-bold text-gray-900 tracking-tight">{formatCurrency(stockDetails.lastPrice)}</span>
              <span className={`text-[10.5px] font-semibold flex items-center gap-1 ${stockDetails.tenDayChange.includes('-') ? 'text-red-600' : 'text-green-600'}`}>
                {stockDetails.tenDayChange.includes('-') ? <TrendingDown size={12} /> : <TrendingUp size={12} />}
                {stockDetails.tenDayChange}
              </span>
            </div>

            {/* Ticker */}
            <div className="text-[10.5px] font-bold text-gray-500 tracking-wide">{stockDetails.ticker}</div>
          </div>

          {/* Footer: Sector & Earnings */}
          <div className="flex flex-col gap-1 pt-2 mt-2 border-t border-gray-100 text-[10.5px] text-gray-600 font-medium">
            <div className="flex items-center gap-1.5">
              <Building2 size={12} className="text-gray-400" />
              <span className="truncate">{stockDetails.sector}</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Calendar size={12} className="text-gray-400" />
              <span>Earnings Date: {stockDetails.earningsDate}</span>
            </div>
          </div>
        </div>

        {/* Section 2: Analyst View (Flex-1) */}
        <div className="flex-1 p-3 bg-gray-50/30 flex flex-col">
          <SectionHeader icon={<Target className="w-3 h-3 text-blue-600" />} title="Analyst View" />
          <div className="space-y-1 mt-1 flex-grow">
            <DataRow label="UBS Rating" value={stockDetails.ubsGrpRating} />
            <DataRow label="Target" value={formatCurrency(stockDetails.ubsGrpTarget)} />
            <DataRow label="CIO Rating" value={stockDetails.ubsCioRating} />
          </div>
        </div>

        {/* Section 3: Key Data (Flex-1) */}
        <div className="flex-1 p-3 flex flex-col">
          <SectionHeader icon={<Activity className="w-3 h-3 text-blue-600" />} title="Key Data" />
          <div className="space-y-1 mt-1 flex-grow">
             <DataRow label="52w High" value={formatCurrency(stockDetails.fiftyTwoWeekHigh).split('.')[0]} />
             <DataRow label="52w Low" value={formatCurrency(stockDetails.fiftyTwoWeekLow).split('.')[0]} />
             <DataRow label="Yield" value={`${stockDetails.dividendYield.toFixed(2)}%`} />
          </div>
        </div>

        {/* Section 4: Client Position (Flex-1.2) */}
        <div className="flex-[1.2] p-3 bg-blue-50/20 flex flex-col">
          <SectionHeader icon={<PieChart className="w-3 h-3 text-blue-600" />} title="Client Position" />
          
          {clientPosition ? (
            <div className="mt-1 space-y-1.5 flex-grow flex flex-col justify-center">
              <div className="flex justify-between items-baseline">
                <span className="text-[10.5px] text-gray-500">Market Value</span>
                <span className="text-[11.5px] font-bold text-gray-900 leading-none">{formatCurrency(clientPosition.mktValue)}</span>
              </div>
              
              <div className="flex justify-between items-center">
                <span className="text-[10.5px] text-gray-500">Total P&L</span>
                <div className={`text-[10.5px] font-bold flex items-center gap-1 ${clientPosition.pnlDollar >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                  <span>{clientPosition.pnlDollar >= 0 ? '+' : ''}{formatCurrency(clientPosition.pnlDollar)}</span>
                  <span className={`text-[9.5px] px-1.5 py-0.5 rounded ${clientPosition.pnlDollar >= 0 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                    {clientPosition.pnlPercent}%
                  </span>
                </div>
              </div>

              <div className="pt-2 border-t border-blue-100 flex justify-between text-[10.5px] text-gray-500 mt-auto">
                 <span>{clientPosition.shares} Shares</span>
                 <span>Avg: {formatCurrency(clientPosition.avgCost)}</span>
              </div>
            </div>
          ) : (
            <div className="mt-2 text-[10.5px] text-gray-400 italic">No existing position</div>
          )}
        </div>

      </div>
    </div>
  );
}

// Sub-components for consistency
function SectionHeader({ icon, title }: { icon: React.ReactNode, title: string }) {
  return (
    <div className="flex items-center gap-1.5 mb-1 h-4">
      {icon}
      <h4 className="text-[10px] font-bold text-gray-500 uppercase tracking-wider">{title}</h4>
    </div>
  );
}

function DataRow({ label, value }: { label: string, value: string }) {
  return (
    <div className="flex justify-between items-baseline text-[10.5px] h-4.5">
      <span className="text-gray-500">{label}</span>
      <span className="font-semibold text-gray-900">{value}</span>
    </div>
  );
}

function formatCurrency(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(value);
}
