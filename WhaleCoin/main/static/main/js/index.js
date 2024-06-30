
function startMining() {
  console.log('1111')
  var circle = document.getElementById('progressCircle');
  var content = document.getElementById('circleContent');
  
  circle.style.setProperty('--progress', 0);
  circle.style.animation = 'fill 5m linear forwards';
  content.innerHTML = 'Mining...';
  
  setTimeout(function() {
      content.innerHTML = 'Complete!';
  }, 5 * 60 * 1000); // 5 minutes
}

// Add the CSS for the animation to the document head
var style = document.createElement('style');
style.innerHTML = `
  @keyframes fill {
      to {
          transform: scaleY(1);
      }
  }

  .progress-circle:before {
      animation: fill 5m linear forwards;
  }
`;
document.head.appendChild(style);
