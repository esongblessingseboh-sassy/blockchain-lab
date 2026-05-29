// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract SimpleStorage {
    uint256 private storedData;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function set(uint256 x) public {
        require(msg.sender == owner, "Not owner");
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}