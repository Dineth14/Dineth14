import type { CSSProperties, ReactNode } from 'react';

type GlowCardProps = {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
};

export function GlowCard({ children, className = '', style }: GlowCardProps) {
  return (
    <div className={`signal-card rounded-[1.6rem] ${className}`.trim()} style={style}>
      {children}
    </div>
  );
}
