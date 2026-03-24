'use client';

import { motion } from 'framer-motion';

type AnimatedTextProps = {
  text: string;
  className?: string;
  delay?: number;
  stagger?: number;
};

export function AnimatedText({
  text,
  className = '',
  delay = 0.2,
  stagger = 0.045,
}: AnimatedTextProps) {
  return (
    <span className={className} aria-label={text}>
      {text.split('').map((character, index) => (
        <motion.span
          key={`${character}-${index}`}
          aria-hidden='true'
          className='inline-block'
          initial={{ opacity: 0, y: '0.8em', filter: 'blur(8px)' }}
          animate={{ opacity: 1, y: '0em', filter: 'blur(0px)' }}
          transition={{
            delay: delay + index * stagger,
            duration: 0.55,
            ease: [0.22, 1, 0.36, 1],
          }}
        >
          {character === ' ' ? '\u00A0' : character}
        </motion.span>
      ))}
    </span>
  );
}
