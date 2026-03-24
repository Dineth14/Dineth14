'use client';

import { motion } from 'framer-motion';
import { Eye, Satellite, Signal, Users } from 'lucide-react';
import { fadeUp, staggerParent } from '@/lib/animations';
import { researchDomains } from '@/lib/site-data';
import { GlowCard } from './ui/GlowCard';
import { RadarSweep } from './ui/RadarSweep';

const iconMap = {
  satellite: Satellite,
  eye: Eye,
  users: Users,
  waveform: Signal,
};

export function Research() {
  return (
    <section id='research' className='relative border-b border-white/5 py-24 sm:py-28'>
      <div className='section-shell'>
        <motion.div
          initial='hidden'
          whileInView='visible'
          viewport={{ once: true, amount: 0.18 }}
          variants={staggerParent}
          className='space-y-12'
        >
          <motion.div
            variants={fadeUp}
            className='flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between'
          >
            <div className='flex items-center gap-5'>
              <RadarSweep className='w-20 shrink-0' />
              <div className='space-y-4'>
                <span className='section-kicker'>Research Domains</span>
                <h2 className='font-display text-4xl leading-tight text-mist sm:text-5xl'>
                  Signal intelligence across earth observation, vision, and embedded
                  sensing.
                </h2>
              </div>
            </div>
            <p className='max-w-xl text-base leading-8 text-mist/66'>
              Current work is organized around spatial reasoning, physically grounded
              inference, and robust perception pipelines that can move from research
              prototypes into constrained systems.
            </p>
          </motion.div>

          <motion.div variants={staggerParent} className='grid gap-6 md:grid-cols-2'>
            {researchDomains.map((domain) => {
              const Icon = iconMap[domain.icon];

              return (
                <motion.div key={domain.title} variants={fadeUp}>
                  <GlowCard className='group h-full p-6 sm:p-7'>
                    <div className='flex h-full flex-col'>
                      <div className='mb-6 flex items-start justify-between gap-4'>
                        <div>
                          <span className='mb-4 inline-flex rounded-full border border-cyan/20 bg-cyan/8 px-3 py-1 text-[0.7rem] uppercase tracking-[0.22em] text-cyan/85'>
                            {domain.tag}
                          </span>
                          <h3 className='max-w-xs font-display text-2xl text-mist'>
                            {domain.title}
                          </h3>
                        </div>
                        <span className='rounded-2xl border border-white/8 bg-white/5 p-3 text-cyan transition group-hover:border-cyan/30 group-hover:bg-cyan/8'>
                          <Icon className='h-6 w-6' />
                        </span>
                      </div>

                      <ul className='space-y-4 text-sm leading-7 text-mist/72'>
                        {domain.bullets.map((bullet) => (
                          <li key={bullet} className='flex gap-3'>
                            <span className='mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-ember shadow-[0_0_14px_rgba(255,107,53,0.8)]' />
                            <span>{bullet}</span>
                          </li>
                        ))}
                      </ul>

                      <div className='mt-8 h-px bg-gradient-to-r from-cyan/0 via-cyan/70 to-cyan/0 transition duration-300 group-hover:via-ember/75' />
                    </div>
                  </GlowCard>
                </motion.div>
              );
            })}
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
