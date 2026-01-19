import { LineChart, Line, XAxis, YAxis, CartesianGrid, ReferenceLine, Label, ResponsiveContainer } from 'recharts';

interface PayoffDiagramProps {
  optionLegs: any[];
  currentPrice: number;
  netPremium: number;
  metrics: any;
}

export function PayoffDiagram({ optionLegs, currentPrice, netPremium, metrics }: PayoffDiagramProps) {
  // Generate payoff data
  const generatePayoffData = () => {
    const data = [];
    const minPrice = 180;
    const maxPrice = 280;
    const step = 2;

    for (let price = minPrice; price <= maxPrice; price += step) {
      let optionPayoff = 0;
      
      // Calculate payoff for each leg
      optionLegs.forEach(leg => {
        const multiplier = leg.action === 'Buy' ? 1 : -1;
        let legPayoff = 0;
        
        if (leg.type === 'Call') {
          legPayoff = Math.max(0, price - leg.strike) * 100;
        } else {
          legPayoff = Math.max(0, leg.strike - price) * 100;
        }
        
        // Subtract premium paid or add premium received
        const premiumEffect = multiplier * leg.premium;
        optionPayoff += (multiplier * legPayoff) + premiumEffect;
      });

      const stockPayoff = (price - 198) * 100; // 100 shares at cost basis $198
      const combinedPayoff = stockPayoff + optionPayoff;

      data.push({
        price,
        optionPayoff,
        stockPayoff,
        combinedPayoff
      });
    }
    
    return data;
  };

  const data = generatePayoffData();

  // Find breakeven points
  const breakevens = [
    { price: 183.4, label: "B/E $183.4" },
    { price: 214.6, label: "B/E $214.6" },
    { price: 265.4, label: "B/E $265.4" }
  ];

  const strikes = [
    { price: 210, label: "210" },
    { price: 230, label: "230" },
    { price: 250, label: "250" },
    { price: 270, label: "270" }
  ];

  return (
    <div className="flex gap-4 items-stretch">
      {/* Left: Chart Section */}
      <div className="flex-grow w-2/3">
        <div className="bg-white border border-gray-200 rounded-lg p-3 h-full">
          <div className="flex justify-between items-center mb-2">
            <h3 className="text-sm font-semibold text-gray-900">Payoff Diagram</h3>
            <div className="text-xs text-gray-500">Spot: ${currentPrice.toFixed(2)}</div>
          </div>
          
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={data} margin={{ top: 10, right: 10, left: 35, bottom: 20 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" vertical={false} />
                <XAxis 
                  dataKey="price" 
                  domain={[180, 280]}
                  ticks={[180, 200, 220, 240, 260, 280]}
                  label={{ value: 'Stock Price', position: 'insideBottom', offset: -10, style: { fontSize: 10, fill: '#6b7280' } }}
                  stroke="#9ca3af"
                  tick={{ fontSize: 9 }}
                />
                <YAxis 
                  domain={[-5000, 10000]}
                  ticks={[-5000, 0, 5000, 10000]}
                  label={{ value: 'P/L $', angle: -90, position: 'insideLeft', style: { fontSize: 10, fill: '#6b7280' } }}
                  stroke="#9ca3af"
                  tick={{ fontSize: 9 }}
                />
                
                {/* Breakeven lines */}
                {breakevens.map((be, idx) => (
                  <ReferenceLine 
                    key={`be-${idx}`}
                    x={be.price} 
                    stroke="#9ca3af" 
                    strokeDasharray="4 2"
                    strokeWidth={1}
                  >
                   {/* Reduced label complexity for cleaner chart */}
                  </ReferenceLine>
                ))}

                {/* Strike lines */}
                {strikes.map((strike, idx) => (
                  <ReferenceLine 
                    key={`strike-${idx}`}
                    x={strike.price} 
                    stroke="#e5e7eb" 
                    strokeWidth={1}
                  />
                ))}

                {/* Zero line */}
                <ReferenceLine y={0} stroke="#000" strokeWidth={1} />

                <Line type="monotone" dataKey="stockPayoff" stroke="#93C5FD" strokeWidth={2} dot={false} />
                <Line type="monotone" dataKey="optionPayoff" stroke="#C4B5FD" strokeWidth={2} dot={false} />
                <Line type="monotone" dataKey="combinedPayoff" stroke="#4B5563" strokeWidth={2} strokeDasharray="4 4" dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
          
          <div className="flex justify-center gap-4 mt-2">
            <div className="flex items-center gap-1.5">
              <div className="w-3 h-0.5 bg-blue-300"></div>
              <span className="text-[10px] text-gray-600">Stock</span>
            </div>
            <div className="flex items-center gap-1.5">
              <div className="w-3 h-0.5 bg-violet-300"></div>
              <span className="text-[10px] text-gray-600">Options</span>
            </div>
            <div className="flex items-center gap-1.5">
              <div className="w-3 h-0.5 bg-gray-600 border-t border-dashed"></div>
              <span className="text-[10px] text-gray-600">Combined</span>
            </div>
          </div>
        </div>
      </div>

      {/* Right: Metrics Section */}
      <div className="w-1/3 flex flex-col gap-2">
        {/* Risk & Reward */}
        <MetricBox title="Risk & Reward">
          <MetricRow label="Max Profit" value={metrics.maxProfit.combined} subValue={metrics.maxProfit.options} />
          <MetricRow label="Max Loss" value={metrics.maxLoss.combined} subValue={metrics.maxLoss.options} isDestructive />
          <MetricRow label="R/R Ratio" value={metrics.rewardRisk.combined} subValue={metrics.rewardRisk.options} />
        </MetricBox>

        {/* Return Metrics */}
        <MetricBox title="Return Metrics">
          <MetricRow label="Max ROI" value={metrics.maxROI.combined} subValue={metrics.maxROI.options} isPercent />
          <MetricRow label="Min ROI" value={metrics.minROI.combined} subValue={metrics.minROI.options} isPercent isDestructive />
        </MetricBox>

        {/* Capital */}
        <MetricBox title="Capital">
          <MetricRow label="Capital Basis" value={metrics.capitalBasis.combined} subValue={metrics.capitalBasis.options} />
          <MetricRow label="Net Cost" value={metrics.costCredit.combined} subValue={metrics.costCredit.options} />
        </MetricBox>

         {/* Premium */}
         <MetricBox title="Premium">
          <MetricRow label="Net Prem/Share" value={metrics.netPremPerShare.combined} />
          <MetricRow label="Yield %" value={metrics.netPremPercent.combined} isPercent />
        </MetricBox>
      </div>
    </div>
  );
}

function MetricBox({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="bg-gray-50 border border-gray-200 rounded-md p-2 flex-1 flex flex-col justify-center">
      <h4 className="text-[10px] font-bold text-gray-500 uppercase tracking-wider mb-1.5 border-b border-gray-200 pb-1">{title}</h4>
      <div className="space-y-1">
        {children}
      </div>
    </div>
  );
}

function MetricRow({ label, value, subValue, isPercent = false, isDestructive = false }: { label: string; value: any; subValue?: any; isPercent?: boolean; isDestructive?: boolean }) {
  const format = (v: any) => {
    if (v === "Unlimited" || v === "N/A" || v === "∞") return v;
    if (typeof v === 'number') {
      if (isPercent) return `${(v * 100).toFixed(2)}%`;
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(v);
    }
    return v;
  };

  const valClass = (v: any) => {
    if (typeof v === 'number' && v < 0) return 'text-red-600';
    return 'text-gray-900';
  };

  return (
    <div className="flex justify-between items-baseline text-[10px]">
      <span className="text-gray-600">{label}</span>
      <div className="text-right">
        <span className={`font-bold ${valClass(value)}`}>{format(value)}</span>
        {subValue !== undefined && (
          <span className="text-[9px] text-gray-400 ml-1.5 hidden xl:inline">({format(subValue)})</span>
        )}
      </div>
    </div>
  );
}
