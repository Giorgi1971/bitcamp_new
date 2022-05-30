gsap.from('.post', {
  scrollTrigger: {
    trigger: '.post',
  },
  duration: 0.5,
  y: 100,
  opacity: 0,
  stagger: 0.2,
  ease: Power3.easeOut,
})
let proxy = { skew: 0 },
  skewSetter = gsap.quickSetter('.post', 'skewY', 'deg'),
  clamp = gsap.utils.clamp(-10, 10)

ScrollTrigger.create({
  onUpdate: (self) => {
    let skew = clamp(self.getVelocity() / -300)
    if (Math.abs(skew) > Math.abs(proxy.skew)) {
      proxy.skew = skew
      gsap.to(proxy, {
        skew: 0,
        duration: 0.8,
        ease: 'power2',
        overwrite: true,
        onUpdate: () => skewSetter(proxy.skew),
      })
    }
  },
})

gsap.set('.post', { transformOrigin: 'right center', force3D: true })
