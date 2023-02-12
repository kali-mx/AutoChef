/**
 *
 * @licstart  The following is the entire license notice for the JavaScript code in this file. 
 *
 * ES6 polyfills that use native implementation if available and do not pollute the global namespace
 o*
 * Copyright (c) 2015-2016 University Of Helsinki (The National Library Of Finland)
 *
 * This file is part of es6-polyfills 
 *
 * es6-polyfills is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * @licend  The above is the entire license notice
 * for the JavaScript code in this page.
 *
 **/

/* istanbul ignore next */
(function (root, factory) {
  
  'use strict';

  if (typeof define === 'function' && define.amd) {
    define(factory);
  } else if (typeof exports === 'object' && module.exports) {
    module.exports = factory();
  }

}(this, factory));

function factory() {     

  'use strict';

  /**
   * Implementation: {@link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of#Polyfill}
   */
  function arrayOf()
  {
    return Array.prototype.slice.call(arguments);
  }

  return function(context)
  {

    var polyfill = function() {};
    
    context = typeof context === 'function' ? context : Object; 

    Object.getOwnPropertyNames(context.prototype).forEach(function(prop) {
      if (typeof context.prototype[prop] === 'function') {
        polyfill.prototype[prop] = context.prototype[prop];
      }
    });

    Object.getOwnPropertyNames(context).forEach(function(prop) {
      if (!polyfill.hasOwnProperty(prop) && typeof context[prop] === 'function') {
        polyfill[prop] = context[prop];
      }
    });

    polyfill.of = arrayOf;

    return polyfill;

  };

}
