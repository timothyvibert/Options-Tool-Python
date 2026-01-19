import { ReportHeader } from "./ReportHeader";
import { StockDetailsSection } from "./StockDetailsSection";
import { OptionStrategySection } from "./OptionStrategySection";
import { PayoffDiagram } from "./PayoffDiagram";
import { KeyLevelsSection } from "./KeyLevelsSection";
import { ScenarioAnalysis } from "./ScenarioAnalysis";
import { Printer, FileText } from "lucide-react";

interface StrategyReportProps {
  data: any;
}

export function StrategyReport({ data }: StrategyReportProps) {
  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="bg-gray-100 min-h-screen p-8 print:p-0 print:bg-white print:min-h-0">
      
      {/* Global Print Styles */}
      <style>{`
        @media print {
          @page {
            size: 8.5in 11in;
            margin: 0;
          }
          body {
            print-color-adjust: exact;
            -webkit-print-color-adjust: exact;
          }
          /* Hide browser default header/footers if possible, though user setting overrides */
        }
      `}</style>

      {/* Control Bar - Hidden when printing */}
      <div className="max-w-[8.5in] mx-auto bg-gray-900 text-white p-4 flex justify-between items-center rounded-t-lg mb-8 shadow-lg print:hidden">
        <div className="flex items-center gap-2">
           <FileText className="text-gray-400" size={20} />
           <span className="font-semibold tracking-wide">UBS Strategy Template</span>
        </div>
        <button 
          onClick={handlePrint}
          className="flex items-center gap-2 bg-blue-600 hover:bg-blue-500 text-white px-4 py-2 rounded-md font-medium transition-colors"
        >
          <Printer size={16} />
          Export PDF
        </button>
      </div>

      {/* PAGE 1 */}
      <PageContainer pageNum={1} totalPages={2}>
        <div className="space-y-3">
          <ReportHeader 
            title={data.strategyName} 
            subtitle="Wealth Management Option Strategy" 
            date={data.date} 
          />
          
          <StockDetailsSection 
            stockDetails={data.stockDetails} 
            clientPosition={data.clientPosition} 
          />
          
          <OptionStrategySection 
            description={data.strategyDescription}
            optionLegs={data.optionLegs}
            netPremium={data.netPremium}
            metrics={data.metrics}
          />
          
          <div className="h-[240px]">
            <PayoffDiagram 
              optionLegs={data.optionLegs}
              currentPrice={data.stockDetails.lastPrice}
              netPremium={data.netPremium}
              metrics={data.metrics}
            />
          </div>
        </div>
      </PageContainer>

      {/* PAGE 2 */}
      <PageContainer pageNum={2} totalPages={2} className="print:mt-0 mt-8">
        <div className="space-y-8 pt-4">
          <ScenarioAnalysis scenarios={data.scenarioAnalysis} />
          <KeyLevelsSection keyLevels={data.keyLevels} commentary={data.keyLevelsCommentary} />
          
          {/* Disclosures / Footer Text */}
          <div className="mt-8 pt-6 border-t border-gray-200">
            <h4 className="text-[10px] font-bold text-gray-900 mb-2">Important Risk Disclosures</h4>
            <p className="text-[9px] text-gray-500 leading-relaxed text-justify">
              Options involve risk and are not suitable for all investors. Please ensure that you have read and understood the current Options Disclosure Document titled "Characteristics and Risks of Standardized Options". 
              This report is for simulation purposes only. Past performance is not a guarantee of future results. The analysis assumes the options are held to expiration, although they may be closed out earlier.
              UBS Financial Services Inc. does not provide tax or legal advice. Please consult with your tax and legal advisors regarding your personal circumstances.
            </p>
          </div>
        </div>
      </PageContainer>

    </div>
  );
}

// ----------------------------------------------------------------------
// Page Container Component
// Enforces 8.5in x 11in dimensions and standard footer
// ----------------------------------------------------------------------

interface PageContainerProps {
  children: React.ReactNode;
  pageNum: number;
  totalPages: number;
  className?: string;
}

function PageContainer({ children, pageNum, totalPages, className = "" }: PageContainerProps) {
  return (
    <div 
      className={`
        mx-auto bg-white shadow-2xl overflow-hidden relative flex flex-col justify-between
        w-[8.5in] h-[11in] 
        print:shadow-none print:w-full print:h-screen print:break-after-page
        ${className}
      `}
    >
      {/* Content Area with standard padding */}
      <div className="px-10 py-8 flex-grow">
        {children}
      </div>

      {/* Standard Footer */}
      <div className="px-10 pb-6 pt-2 flex justify-between items-end text-[9px] text-gray-400 uppercase font-medium tracking-wider">
        <span>UBS Financial Services Inc.</span>
        <span>Page {pageNum} of {totalPages}</span>
      </div>
    </div>
  );
}
