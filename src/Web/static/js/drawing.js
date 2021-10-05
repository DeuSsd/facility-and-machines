import anime from 'animejs/lib/anime.es.js';

/*
anime({
    targets: 'div',
    translateX: 250,
    rotate: '1turn',
    backgroundColor: '#FFF',
    duration: 800
});
*/

const path = anime.path('animejs/lib/anime.es.js');

const timeline = anime.timeline({
  easing: 'easeInOutExpo',
  duration: 1000,
  complete: () => {
    anime({
      targets: '.leaf',
      rotate: 40,
      duration: 3000,
      loop: true,
      direction: 'alternate',
      easing: 'easeInOutQuad'
    });
    anime({
      targets: '.petals',
      scale: 1.05,
      duration: 6000,
      loop: true,
      direction: 'alternate',
      easing: 'easeInOutQuad'
    });
  }
});

timeline.add({
  targets: '.stem',
  scale: [0, 1],
})

timeline.add({
  targets: '.leaf',
  rotate: [0, 45],
})
timeline.add({
  targets: '.petals',
  scale: [0, 1],
}, '-=1000');

timeline.add({
  targets: '#bee',
  opacity: [0, 1],
}, '-=750');


anime({
  targets: '#bee',
  translateX: path('x'),
  translateY: path('y'),
  rotate: path('angle'),
  loop: true,
  duration: 12500,
  easing: 'linear'
});