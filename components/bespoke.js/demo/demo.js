(function() {
	'use strict';

	var themes,
		selectedThemeIndex,
		instructionsTimeout,
		deck;

	function init() {
		// deck = bespoke.from('article');
		// initThemeSwitching();
		bespoke.horizontal.from('article');
	}

	init();

	function initThemeSwitching() {
		themes = [
			'coverflow'
		];
		
		selectedThemeIndex = 0;

		// initInstructions();
		initKeys();
		// initSlideGestures();
		// initThemeGestures();
		// initButtons();

		// selectTheme(0);
	}


	function initKeys() {
		if (/Firefox/.test(navigator.userAgent)) {
			document.addEventListener('keydown', function(e) {
				if (e.which >= 37 && e.which <= 40) {
					e.preventDefault();
				}
			});
		}

		document.addEventListener('keydown', function(e) {
			var key = e.which;

			key === 37 && deck.prev();
			(key === 32 || key === 39) && deck.next();

			key === 38 && prevTheme();
			key === 40 && nextTheme();
		});
	}

	

	// function initButtons() {
	// 	document.getElementById('up-arrow').addEventListener('click', prevTheme);
	// 	document.getElementById('down-arrow').addEventListener('click', nextTheme);
	// }

	// function selectTheme(index) {
	// 	var theme = themes[index];
	// 	document.body.className = theme;
	// 	document.getElementById('theme').innerHTML = theme[0].toUpperCase() + theme.slice(1);
	// 	selectedThemeIndex = index;
	// }

	// function nextTheme() {
	// 	offsetSelectedTheme(1);
	// 	hideInstructions();
	// }

	// function prevTheme() {
	// 	offsetSelectedTheme(-1);
	// 	hideInstructions();
	// }

	function offsetSelectedTheme(n) {
		selectTheme(modulo(selectedThemeIndex + n, themes.length));
	}

	function showInstructions() {
		document.querySelectorAll('header p')[0].className = 'visible';
	}

	function hideInstructions() {
		clearTimeout(instructionsTimeout);
		document.querySelectorAll('header p')[0].className = 'hidden';
	}

	function isTouch() {
		return !!('ontouchstart' in window) || navigator.msMaxTouchPoints;
	}

	function modulo(num, n) {
		return ((num % n) + n) % n;
	}

}());