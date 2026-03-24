'use client';

import { motion } from 'framer-motion';
import { fadeUp, staggerParent } from '@/lib/animations';

const codeLines = [
  ['class', 'DinethPerera', ':'],
  ['role', '=', '"Electronics Engineering Undergraduate"'],
  ['location', '=', '"Sri Lanka 🇱🇰"'],
  ['focus', '=', '["AI for Perception", "Vision Mamba",'],
  ['', '', '"Remote Sensing", "Embedded AI"]'],
  ['hardware', '=', '["ESP32", "AVR", "ARM", "Raspberry Pi"]'],
  ['research', '=', '["Change Detection", "GAR", "SSMs"]'],
  ['email', '=', '"dp18perera@gmail.com"'],
  ['status', '=', '"🔬 Active research - seeking collaborations"'],
] as const;

export function About() {
  return (
    <section id='about' className='relative border-b border-white/5 py-24 sm:py-28'>
      <div className='section-shell'>
        <motion.div
          initial='hidden'
          whileInView='visible'
          viewport={{ once: true, amount: 0.25 }}
          variants={staggerParent}
          className='grid gap-12 lg:grid-cols-[minmax(0,1.05fr)_minmax(320px,0.95fr)] lg:gap-14'
        >
          <motion.div variants={fadeUp} className='space-y-8'>
            <span className='section-kicker'>About</span>
            <h2 className='max-w-3xl font-display text-4xl leading-tight text-mist sm:text-5xl lg:text-6xl'>
              I build theory-backed, system-level solutions that scale from hardware to
              algorithms.
            </h2>
            <p className='max-w-2xl text-base leading-8 text-mist/70 sm:text-lg'>
              My work spans embedded intelligence, remote sensing AI, and physically
              grounded activity recognition. I care about robust sensing, principled
              modeling, and systems that survive contact with real-world constraints.
            </p>
          </motion.div>

          <motion.div variants={fadeUp} className='code-panel rounded-[1.8rem] p-6 sm:p-8'>
            <div className='mb-6 flex items-center gap-3 text-[0.7rem] uppercase tracking-[0.28em] text-mist/55'>
              <span className='h-2.5 w-2.5 rounded-full bg-ember' />
              <span className='h-2.5 w-2.5 rounded-full bg-yellow-400' />
              <span className='h-2.5 w-2.5 rounded-full bg-cyan' />
              profile.py
            </div>
            <pre className='overflow-x-auto font-mono text-sm leading-8 text-mist/84'>
              {codeLines.map((line, index) => {
                const [key, operator, value] = line;
                const indent = index === 0 ? '' : '    ';

                if (index === 0) {
                  return (
                    <div key={line.join('-')}>
                      <span className='token-key'>{key}</span>{' '}
                      <span className='token-class'>{operator}</span>
                      {value}
                    </div>
                  );
                }

                return (
                  <div key={`${key}-${index}`}>
                    {indent}
                    {key ? <span className='token-key'>{key}</span> : <span>     </span>}{' '}
                    {operator ? <span className='token-op'>{operator}</span> : null}{' '}
                    <span className={value.startsWith('[') ? 'token-array' : 'token-string'}>
                      {value}
                    </span>
                  </div>
                );
              })}
            </pre>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
