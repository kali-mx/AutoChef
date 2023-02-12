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

(function (root, factory) {
  
  'use strict';

  if (typeof define === 'function' && define.amd) {
    define(['chai/chai', '../lib/promise'], factory);
  } else if (typeof exports === 'object' && module.exports) {
    module.exports = factory(require('chai'), require('../lib/promise'));
  }

}(this, factory));

function factory(chai, createPolyfill) {

  'use strict';

  var expect = chai.expect;
  
  describe('promise', function() {
    
    describe('factory', function() {

      it('Should be a function', function() {
        expect(createPolyfill).to.be.a('function');
      });

      it('Should create a constructor function with methods', function() {

        var Polyfill = createPolyfill();
        
        expect(Polyfill).to.have.ownProperty('resolve');
        expect(Polyfill).to.have.ownProperty('reject');
        expect(Polyfill).to.have.ownProperty('all');
        expect(Polyfill).to.have.ownProperty('race');
        
        expect(Polyfill.resolve).to.be.a('function');
        expect(Polyfill.reject).to.be.a('function');
        expect(Polyfill.all).to.be.a('function');
        expect(Polyfill.race).to.be.a('function');

      });

      describe('constructor', function() {

        it('Should instantiate the correct object', function() {
          
          var Polyfill = createPolyfill();
          
          expect(new Polyfill(function(){})).to.respondTo('then').and.to.respondTo('catch');
          expect(new Polyfill(function(){})).to.be.an.instanceOf(Polyfill);

        });

        it('Should resolve', function(done) {

          var Polyfill = createPolyfill();
          
          new Polyfill(function(fn_resolve) {
            
            fn_resolve('foobar');
            
          }).then(function(value) {
            try {
              expect(value).to.eql('foobar');
              done();
            } catch (e) {
              done(e);
            } 
          });

        });

      });

    });

  });

}
