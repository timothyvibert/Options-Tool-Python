interface KeyLevelsSectionProps {
  keyLevels: any[];
  commentary: any[];
}

export function KeyLevelsSection({ keyLevels }: KeyLevelsSectionProps) {
  return (
    <div>
      <h2 className="text-lg text-[#E60000] mb-4 pb-1.5 border-b-2 border-[#E60000]">Option Strategy Key Levels</h2>
      
      {/* Scenario Analysis Table */}
      <div className="mb-6 overflow-hidden border border-gray-300 rounded-lg">
        <table className="w-full text-[10px]">
          <thead className="bg-gray-100">
            <tr>
              <th className="px-1.5 py-1.5 text-left font-semibold text-gray-700 border-b border-gray-300">Scenario</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Price</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Move %</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Stock PnL</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Option PnL</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Option ROI</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Net PnL</th>
              <th className="px-1.5 py-1.5 text-right font-semibold text-gray-700 border-b border-gray-300">Net ROI</th>
            </tr>
          </thead>
          <tbody>
            {keyLevels.map((level, index) => (
              <tr 
                key={index} 
                className={`border-b border-gray-200 last:border-b-0 ${
                  level.scenario === 'Current Market Price' ? 'bg-yellow-50' : ''
                }`}
              >
                <td className="px-1.5 py-1.5 text-gray-900 font-medium">{level.scenario}</td>
                <td className="px-1.5 py-1.5 text-right text-gray-900">{formatValue(level.price)}</td>
                <td className={`px-1.5 py-1.5 text-right ${getColorClass(level.movePercent)}`}>
                  {level.movePercent}
                </td>
                <td className={`px-1.5 py-1.5 text-right ${getColorClass(level.stockPnL)}`}>
                  {formatCurrency(level.stockPnL)}
                </td>
                <td className={`px-1.5 py-1.5 text-right ${getColorClass(level.optionPnL)}`}>
                  {formatCurrency(level.optionPnL)}
                </td>
                <td className={`px-1.5 py-1.5 text-right ${getColorClass(level.optionROI)}`}>
                  {level.optionROI}
                </td>
                <td className={`px-1.5 py-1.5 text-right font-semibold ${getColorClass(level.netPnL)}`}>
                  {formatCurrency(level.netPnL)}
                </td>
                <td className={`px-1.5 py-1.5 text-right font-semibold ${getColorClass(level.netROI)}`}>
                  {level.netROI}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function formatValue(value: any): string {
  if (value === "---" || value === "∞") return value;
  if (typeof value === 'number') {
    return `$${value.toFixed(2)}`;
  }
  return value;
}

function formatCurrency(value: any): string {
  if (value === "Unlimited" || value === "∞") return value;
  if (typeof value !== 'number') return value;
  
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(value);
}

function getColorClass(value: any): string {
  if (typeof value === 'string') {
    if (value.includes('-') && value !== '---') return 'text-red-600';
    return 'text-gray-900';
  }
  if (typeof value === 'number') {
    return value < 0 ? 'text-red-600' : 'text-gray-900';
  }
  return 'text-gray-900';
}
