import { Circle } from "lucide-react";

interface Scenario {
  title: string;
  condition: string;
  description: string;
  type: "bearish" | "stagnant" | "bullish";
}

interface ScenarioAnalysisProps {
  scenarios: Scenario[];
}

export function ScenarioAnalysis({ scenarios }: ScenarioAnalysisProps) {
  const getDotColor = (type: string) => {
    switch (type) {
      case "bearish":
        return "text-[#E60000]"; // Red
      case "bullish":
        return "text-[#00A550]"; // Green
      default:
        return "text-gray-400"; // Grey
    }
  };

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-5 shadow-sm break-inside-avoid">
      <h3 className="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wide border-b border-gray-100 pb-2">
        Scenario Analysis
      </h3>
      
      {/* 
         Fixed: Added 'print:grid-cols-3' to ensure it stays 3 columns in PDF.
         Added 'items-stretch' to make boxes equal height.
      */}
      <div className="grid grid-cols-1 md:grid-cols-3 print:grid-cols-3 gap-4 items-stretch">
        {scenarios.map((scenario, index) => (
          <div 
            key={index} 
            className="border border-gray-200 bg-gray-50/50 rounded p-3 flex flex-col h-full break-inside-avoid"
          >
            {/* Header */}
            <div className="flex items-center gap-2 mb-2">
              <Circle className={`w-2.5 h-2.5 fill-current ${getDotColor(scenario.type)}`} />
              <h4 className="font-bold text-gray-900 text-xs">{scenario.title}</h4>
            </div>
            
            {/* Condition */}
            <div className="text-[10px] font-semibold text-gray-700 mb-1.5 bg-white border border-gray-100 px-2 py-1 rounded self-start">
              {scenario.condition}
            </div>
            
            {/* Description */}
            <p className="text-[10px] text-gray-600 leading-relaxed mt-auto">
              {scenario.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
