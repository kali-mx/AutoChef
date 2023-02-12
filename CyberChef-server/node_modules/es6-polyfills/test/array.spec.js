/**
 *
 * @licstart  The following is the entire license notice for the JavaScript code in this file. 
 *
 * ES6 polyfills that use native implementation if available and do not pollute the global namespace
 *
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
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * @licend  The above is the entire license notice
 * for the JavaScript code in this page.
 *
 **/

(function (root, factory) {
  
  'use strict';

  if (typeof define === 'function' && define.amd) {
    define(['chai/chai', '../lib/array'], factory);
  } else if (typeof exports === 'object' && module.exports) {
    module.exports = factory(require('chai'), require('../lib/array'));
  }

}(this, factory));

function factory(chai, createPolyfill) {

  'use strict';

  var expect = chai.expect;
  
  describe('array', function() { 

    describe('factory', function() {

      it('Should be a function', function() {
        expect(createPolyfill).to.be.a('function');
      });

      describe('constructor', function() {

        it('Should instantiate the correct object', function() {

          var Polyfill = createPolyfill(function() {}),
          obj = new Polyfill();     

          expect(obj).to.be.an('object');

        });

        it('Should instantiate the correct object (With native Array)', function() {

          var Polyfill = createPolyfill(),
          obj = new Polyfill();     
          
          expect(obj).to.be.an('object');

        });

        it("Should create a new property 'of' which is a function", function() {
          
          var Polyfill,
          constructor = function() {};
          
          constructor.test = function() {};
          Polyfill = createPolyfill(constructor);
          
          expect(Polyfill).to.be.a('function');
          expect(Polyfill.test).to.be.a('function');
          expect(Polyfill.of).to.be.a('function');
          expect(new Polyfill()).to.be.a('object');
          expect(new Polyfill()).to.be.an.instanceof(Polyfill);
          
        });
        
        it('Should create a new Array instance of variadic arguments', function() {

          var polyfill = createPolyfill(function(){}),
          arr = polyfill.of(1, 2, 3);
          
          expect(arr).to.be.an('array');
          expect(arr).to.eql([1, 2, 3]);
          
        });

      });
      
    });
    
  });

}
