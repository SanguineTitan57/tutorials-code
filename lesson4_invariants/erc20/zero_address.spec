methods{
    function balanceOf(address) external returns (uint256) envfree;
}

invariant addressZeroWillHaveZeroBalance
    balanceOf(0) == 0;