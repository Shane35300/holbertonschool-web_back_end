const Utils = {
	calculateNumber: function (type, a, b) {
	  if (type === 'SUM') {
		return Math.round(a) + Math.round(b);
	  } else if (type === 'SUBTRACT') {
		return Math.round(a) - Math.round(b);
	  } else if (type === 'DIVIDE') {
		const bRounded = Math.round(b);
		if (bRounded === 0) {
		  return 'Error';
		}
		return Math.round(a) / bRounded;
	  }
	}
  };

  module.exports = Utils;
