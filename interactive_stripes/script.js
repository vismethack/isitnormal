function toggleHistory() {
    const el = document.getElementById("history");
    el.classList.toggle("open");
  }
  
  const el = document.getElementById("average");
  el.addEventListener("click", toggleHistory, false);
  
  // Weather data fro Prayagraj.
  const d = [
    {
      "temp": "3.195408509521803353e+01"
    },
    {
      "temp": "2.991741781693002622e+01"
    },
    {
      "temp": "3.112525412411497427e+01"
    },
    {
      "temp": "3.288720090212183322e+01"
    },
    {
      "temp": "3.046141110218923131e+01"
    },
    {
      "temp": "2.918586747623811561e+01"
    },
    {
      "temp": "2.809943739580631927e+01"
    },
    {
      "temp": "3.086532027965637326e+01"
    },
    {
      "temp": "3.076726140420191768e+01"
    },
    {
      "temp": "2.995477357900790594e+01"
    },
    {
      "temp": "3.044740269141004774e+01"
    },
    {
      "temp": "3.050343633452683889e+01"
    },
    {
      "temp": "2.939443714783965333e+01"
    },
    {
      "temp": "2.997345146004687422e+01"
    },
    {
      "temp": "2.972130006602117192e+01"
    },
    {
      "temp": "3.075792246368246197e+01"
    },
    {
      "temp": "2.980068106043665921e+01"
    },
    {
      "temp": "2.998823811586936472e+01"
    },
    {
      "temp": "3.088166342556542077e+01"
    },
    {
      "temp": "3.006450613011168116e+01"
    },
    {
      "temp": "2.841151365816529051e+01"
    },
    {
      "temp": "3.078282630506771511e+01"
    },
    {
      "temp": "3.193307247904920132e+01"
    },
    {
      "temp": "3.139608339917964486e+01"
    },
    {
      "temp": "3.006061490489526022e+01"
    },
    {
      "temp": "3.079605647080359176e+01"
    },
    {
      "temp": "3.108011591160419584e+01"
    },
    {
      "temp": "3.117117058166900279e+01"
    },
    {
      "temp": "3.057270014337962039e+01"
    },
    {
      "temp": "3.129491154355201843e+01"
    },
    {
      "temp": "3.088088518052211384e+01"
    },
    {
      "temp": "3.088788938591176247e+01"
    },
    {
      "temp": "3.125599929138758171e+01"
    },
    {
      "temp": "3.304674113599617158e+01"
    },
    {
      "temp": "2.999290758612909258e+01"
    },
    {
      "temp": "3.123732141034861343e+01"
    },
    {
      "temp": "3.057036540824969961e+01"
    },
    {
      "temp": "3.013610467409432658e+01"
    },
    {
      "temp": "2.922477972840260918e+01"
    },
    {
      "temp": "3.307864918277101651e+01"
    },
    {
      "temp": "3.251208679125642220e+01"
    },
    {
      "temp": "3.116572286636602485e+01"
    },
    {
      "temp": "3.217977615777192568e+01"
    },
    {
      "temp": "3.282727603378856429e+01"
    }
  ];
  
  const history = document.getElementById("historical-days");
  
  // When the weather data starts.
  let year = 1979;
  
  const mean = Math.round(d3.mean(d, d=>d.temp));
  const domain = [d3.min(d, d=>d.temp), d3.max(d, d=>d.temp)];
  
  // Blue to Red color scheme.
  const color_scale = d3.scaleSequential().domain([d3.max(d, d=>d.temp), d3.min(d, d=>d.temp)]).interpolator(d3.interpolateRdBu);
  
  const today = document.getElementById("today-temp");
  today.textContent = 43 + ' C';
  today.style.backgroundColor = color_scale(43);
  
  const average = document.getElementById("average-temp");
  average.innerText = Math.round(mean) + ' C';
  
  for (let i = 0; i < d.length; i++) {
    const day = document.createElement('div');
    const temperature =  Number.parseFloat(d[i].temp).toFixed(1);
    day.title = (year + i) + ': ' + temperature.toString() + ' C';
    day.classList.add('day');
    day.style.backgroundColor = color_scale(temperature);
    history.append(day);
  }