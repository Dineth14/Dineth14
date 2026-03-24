'use client';

import Image from 'next/image';
import { motion } from 'framer-motion';
import { fadeUp, staggerParent } from '@/lib/animations';
import { githubStats } from '@/lib/site-data';

export function GitHubStats() {
  return (
    <section id='github' className='relative border-b border-white/5 py-24 sm:py-28'>
      <div className='section-shell'>
        <motion.div
          initial='hidden'
          whileInView='visible'
          viewport={{ once: true, amount: 0.2 }}
          variants={staggerParent}
          className='space-y-12'
        >
          <motion.div variants={fadeUp} className='space-y-5'>
            <span className='section-kicker'>GitHub Signal</span>
            <h2 className='max-w-4xl font-display text-4xl leading-tight text-mist sm:text-5xl'>
              A live telemetry layer for public code, streaks, and contribution rhythm.
            </h2>
          </motion.div>

          <motion.div variants={staggerParent} className='grid gap-6 lg:grid-cols-2'>
            {githubStats.map((card, index) => (
              <motion.div
                key={card.title}
                variants={fadeUp}
                className={index === 2 ? 'lg:col-span-2' : ''}
              >
                <div className='stat-frame rounded-[1.7rem] p-4 sm:p-5'>
                  <p className='mb-4 text-[0.72rem] uppercase tracking-[0.28em] text-cyan/78'>
                    {card.title}
                  </p>
                  <div className='overflow-hidden rounded-[1.25rem] border border-white/6 bg-[#0d1117]'>
                    <Image
                      src={card.src}
                      alt={card.title}
                      width={card.width}
                      height={card.height}
                      className='h-auto w-full'
                      unoptimized
                    />
                  </div>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
