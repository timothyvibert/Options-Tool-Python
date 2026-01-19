interface ReportHeaderProps {
  title: string;
  subtitle: string;
  date: string;
}

export function ReportHeader({ title, subtitle, date }: ReportHeaderProps) {
  return (
    <div className="mb-4">
      {/* Top Row: Logo Left, Metadata Right */}
      <div className="flex items-end justify-between mb-4">
        {/* Left: UBS Logo */}
        <div className="flex items-center gap-2.5">
          <svg width="36" height="36" viewBox="0 0 48 48" fill="none">
            {/* Keys Icon */}
            <path d="M26.5 15.5L34 8L36.5 10.5L29 18L26.5 15.5Z" fill="black"/>
            <path d="M22.5 19.5L30 12L32.5 14.5L25 22L22.5 19.5Z" fill="black"/>
            <path d="M18.5 23.5L26 16L28.5 18.5L21 26L18.5 23.5Z" fill="black"/>
            
            {/* Logo Outline */}
            <path d="M12 24C12 17.3726 17.3726 12 24 12C30.6274 12 36 17.3726 36 24C36 30.6274 30.6274 36 24 36C17.3726 36 12 30.6274 12 24Z" stroke="black" strokeWidth="2.5"/>
            <path d="M12 24H36" stroke="black" strokeWidth="2.5"/>
            <path d="M24 12V36" stroke="black" strokeWidth="2.5"/>
            <path d="M15.5 15.5L32.5 32.5" stroke="black" strokeWidth="2.5"/>
            <path d="M32.5 15.5L15.5 32.5" stroke="black" strokeWidth="2.5"/>
          </svg>
          
          {/* UBS Text */}
          <span className="text-[#E60000] font-bold text-4xl leading-none tracking-tight">
            UBS
          </span>
        </div>
        
        {/* Right: Date & Subtitle */}
        <div className="text-right">
          <div className="text-[10.5px] font-medium text-gray-600 mb-0.5">{date}</div>
          <div className="text-[10.5px] font-bold text-gray-900 tracking-tight">{subtitle}</div>
        </div>
      </div>

      {/* Strategy Title */}
      <h1 className="text-2xl font-bold text-[#E60000] mb-2 tracking-tight leading-none">
        {title}
      </h1>

      {/* Disclaimer Text - Size 9.5px */}
      <p className="text-[9.5px] text-gray-500 leading-snug text-justify max-w-full font-medium">
        The illustration is intended for informational and internal use. Although it can be shared with clients approved for trading Options or have received a copy of the Option Disclosure Document. For specific stock ratings relative to UBS INV research, CIO research, and/or SPGMI's Quality ranking, please refer to the research tab on ConsultWorks. Commissions or fees not included.
      </p>
    </div>
  );
}
