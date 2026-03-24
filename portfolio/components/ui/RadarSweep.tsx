type RadarSweepProps = {
  className?: string;
};

export function RadarSweep({ className = '' }: RadarSweepProps) {
  return (
    <div className={`radar-panel aspect-square ${className}`.trim()}>
      <div className='absolute inset-[18%] rounded-full border border-cyan/20' />
      <div className='absolute inset-[34%] rounded-full border border-cyan/15' />
      <div className='absolute left-1/2 top-[10%] h-[80%] w-px -translate-x-1/2 bg-cyan/10' />
      <div className='absolute left-[10%] top-1/2 h-px w-[80%] -translate-y-1/2 bg-cyan/10' />
      <div className='radar-sweep'>
        <div className='h-full w-full origin-bottom rounded-full bg-[conic-gradient(from_180deg,rgba(0,231,255,0.25),transparent_28%)]' />
      </div>
      <div className='absolute left-1/2 top-1/2 h-2 w-2 -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan shadow-[0_0_18px_rgba(0,231,255,0.9)]' />
    </div>
  );
}
