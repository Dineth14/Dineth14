'use client';

import { Canvas, useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import type { Points as ThreePoints } from 'three';

function SignalField() {
  const points = useRef<ThreePoints>(null);
  const positions = useMemo(() => {
    const array = new Float32Array(600 * 3);

    for (let index = 0; index < 600; index += 1) {
      const stride = index * 3;
      array[stride] = (Math.random() - 0.5) * 12;
      array[stride + 1] = (Math.random() - 0.5) * 7;
      array[stride + 2] = (Math.random() - 0.5) * 6;
    }

    return array;
  }, []);

  useFrame((state) => {
    if (!points.current) {
      return;
    }

    points.current.rotation.z = state.clock.elapsedTime * 0.06;
    points.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.16) * 0.08;
  });

  return (
    <points ref={points}>
      <bufferGeometry>
        <bufferAttribute
          attach='attributes-position'
          count={positions.length / 3}
          array={positions}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial
        color='#00e7ff'
        size={0.045}
        sizeAttenuation
        transparent
        opacity={0.75}
      />
    </points>
  );
}

export default function SignalScene() {
  return (
    <div className='absolute inset-0 z-0 hidden lg:block'>
      <Canvas camera={{ position: [0, 0, 6.4], fov: 54 }} dpr={[1, 1.5]}>
        <ambientLight intensity={0.35} />
        <SignalField />
      </Canvas>
    </div>
  );
}
