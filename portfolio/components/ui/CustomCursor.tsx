'use client';

import { useEffect, useRef, useState } from 'react';

export function CustomCursor() {
  const [enabled, setEnabled] = useState(false);
  const [active, setActive] = useState(false);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const target = useRef({ x: 0, y: 0 });
  const current = useRef({ x: 0, y: 0 });

  useEffect(() => {
    if (window.matchMedia('(pointer: coarse)').matches) {
      return;
    }

    setEnabled(true);

    const updateTarget = (event: MouseEvent) => {
      target.current = { x: event.clientX, y: event.clientY };
    };

    const handleOver = (event: MouseEvent) => {
      const element = event.target as HTMLElement | null;
      setActive(Boolean(element?.closest("a, button, [data-cursor='active']")));
    };

    let frame = 0;
    const loop = () => {
      current.current = {
        x: current.current.x + (target.current.x - current.current.x) * 0.18,
        y: current.current.y + (target.current.y - current.current.y) * 0.18,
      };
      setPosition(current.current);
      frame = window.requestAnimationFrame(loop);
    };

    frame = window.requestAnimationFrame(loop);
    window.addEventListener('mousemove', updateTarget);
    window.addEventListener('mouseover', handleOver);

    return () => {
      window.cancelAnimationFrame(frame);
      window.removeEventListener('mousemove', updateTarget);
      window.removeEventListener('mouseover', handleOver);
    };
  }, []);

  if (!enabled) {
    return null;
  }

  return (
    <>
      <div
        className='cursor-core'
        style={{ transform: `translate3d(${position.x}px, ${position.y}px, 0)` }}
      />
      <div
        className={`cursor-ring ${active ? 'active' : ''}`.trim()}
        style={{ transform: `translate3d(${position.x}px, ${position.y}px, 0)` }}
      />
    </>
  );
}
