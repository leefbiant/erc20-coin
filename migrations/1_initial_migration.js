const Doge = artifacts.require("Doge");

module.exports = function (deployer) {
  deployer.deploy(Doge);
};
