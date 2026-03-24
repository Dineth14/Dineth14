'use client';

import { motion } from 'framer-motion';
import { BrainCircuit, Code2, Cpu, Orbit, Wrench } from 'lucide-react';
import { fadeUp, staggerParent } from '@/lib/animations';
import { techGroups } from '@/lib/site-data';
import { GlowCard } from './ui/GlowCard';

const iconMap = {
  code: Code2,
  brain: BrainCircuit,
  cpu: Cpu,
  tool: Wrench,
  orbit: Orbit,
};

export function TechStack() {
  return (
    <section id='stack' className='relative border-b border-white/5 py-24 sm:py-28'>
      <div className='section-shell'>
        <motion.div
          initial='hidden'
          whileInView='visible'
          viewport={{ once: true, amount: 0.2 }}
          variants={staggerParent}
          className='space-y-12'
        >
          <motion.div variants={fadeUp} className='space-y-5'>
            <span className='section-kicker'>Technical Arsenal</span>
            <h2 className='max-w-4xl font-display text-4xl leading-tight text-mist sm:text-5xl'>
              The tooling stack behind research experiments, embedded prototypes, and
              deployment-ready systems.
            </h2>
          </motion.div>

          <motion.div variants={staggerParent} className='grid gap-6 lg:grid-cols-2'>
            {techGroups.map((group) => {
              const Icon = iconMap[group.icon];

              return (
                <motion.div key={group.title} variants={fadeUp}>
                  <GlowCard className='h-full rounded-[1.8rem] p-6 sm:p-7'>
                    <div className='mb-6 flex items-center gap-4'>
                      <span className='rounded-2xl border border-cyan/18 bg-cyan/10 p-3 text-cyan'>
                        <Icon className='h-6 w-6' />
                      </span>
                      <div>
                        <p className='text-[0.7rem] uppercase tracking-[0.28em] text-cyan/70'>
                          Stack Group
                        </p>
                        <h3 className='mt-2 font-display text-2xl text-mist'>
                          {group.title}
                        </h3>
                      </div>
                    </div>

                    <div className='grid grid-cols-2 gap-3'>
                      {group.items.map((item, index) => (
                        <motion.div
                          key={item}
                          initial={{ opacity: 0, scale: 0.92 }}
                          whileInView={{ opacity: 1, scale: 1 }}
                          viewport={{ once: true }}
                          transition={{
                            delay: index * 0.05,
                            duration: 0.45,
                            ease: [0.22, 1, 0.36, 1],
                          }}
                          className='rounded-2xl border border-white/8 bg-white/5 px-4 py-4 text-sm uppercase tracking-[0.16em] text-mist/78 shadow-[inset_0_1px_0_rgba(255,255,255,0.02)] transition hover:border-cyan/28 hover:text-cyan'
                        >
                          {item}
                        </motion.div>
                      ))}
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
