const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function () {
  let consoleSpy;

  // Utilisation des hooks beforeEach et afterEach
  beforeEach(function () {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    consoleSpy.restore();
  });

  it('should log "The total is: 120" and be called once with 100 and 20', function () {
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 120');
  });

  it('should log "The total is: 20" and be called once with 10 and 10', function () {
    sendPaymentRequestToApi(10, 10);

    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 20');
  });
});
