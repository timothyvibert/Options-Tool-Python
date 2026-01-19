interface OptionStrategySectionProps {
  description: string;
  optionLegs: any[];
  netPremium: number;
  metrics: any;
}

export function OptionStrategySection({ description, optionLegs, netPremium, metrics }: OptionStrategySectionProps) {
  return (
    <div className="mb-4">
      <h2 className="text-base text-[#E60000] mb-2 pb-1 border-b border-[#E60000] font-bold">Option Strategy Details</h2>
      
      <p className="text-[10.5px] text-gray-700 mb-3 leading-relaxed text-justify">{description}</p>

      {/* Option Legs Table */}
      <div className="mb-2">
        <div className="text-[10.5px] font-semibold text-gray-900 mb-1.5">
          Option Leg(s) for Rev Iron Condor strategy (254 DTE) on AMZN
        </div>
        
        <div className="overflow-hidden border border-gray-300 rounded">
          <table className="w-full text-[10.5px]">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-1.5 py-1.5 text-left font-semibold text-gray-700 border-b border-gray-300"></th>
                <th className="px-1.5 py-1.5 text-left font-semibold text-gray-700 border-b border-gray-300">Action</th>
                <th className="px-1.5 py-1.5 text-left font-semibold text-gray-700 border-b border-gray-300">Expiration</th>
                <th className="px-1.5 py-1.5 text-left font-semibold text-gray-700 border-b border-gray-300">Strike</th>
                <th className="px-1.5 py-1.5 text-left font-semibold text-gray-700 border-b border-gray-300">Type</th>
                <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Price</th>
                <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Delta</th>
                <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">OTM %</th>
                <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Premium</th>
              </tr>
            </thead>
            <tbody>
              {optionLegs.map((leg, index) => (
                <tr key={index} className="border-b border-gray-200 last:border-b-0">
                  <td className="px-1.5 py-1.5 text-gray-900">{leg.leg})</td>
                  <td className="px-1.5 py-1.5 text-gray-900">{leg.action} {leg.quantity}</td>
                  <td className="px-1.5 py-1.5 text-gray-900">{leg.expiration}</td>
                  <td className="px-1.5 py-1.5 text-gray-900">${leg.strike}</td>
                  <td className="px-1.5 py-1.5 text-gray-900">{leg.type}</td>
                  <td className="px-1.5 py-1.5 text-right text-gray-900">at ${leg.price.toFixed(2)}</td>
                  <td className="px-1.5 py-1.5 text-right text-gray-900">{leg.delta.toFixed(2)}</td>
                  <td className="px-1.5 py-1.5 text-right text-gray-900">{leg.otmPercent}</td>
                  <td className={`px-1.5 py-1.5 text-right font-semibold ${leg.premium < 0 ? 'text-red-600' : 'text-gray-900'}`}>
                    {formatCurrency(leg.premium)}
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot className="bg-gray-50 border-t border-gray-300">
              <tr>
                <td colSpan={8} className="px-1.5 py-1.5 text-right font-semibold text-gray-900">Net Premium:</td>
                <td className={`px-1.5 py-1.5 text-right font-bold ${netPremium < 0 ? 'text-red-600' : 'text-gray-900'}`}>
                  {formatCurrency(netPremium)}
                </td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  );
}

function formatCurrency(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2
  }).format(value);
}
