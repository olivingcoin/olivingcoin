// Copyright (c) 2016-2018 The Olivingcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef OLIVINGCOIN_WALLET_TEST_WALLET_TEST_FIXTURE_H
#define OLIVINGCOIN_WALLET_TEST_WALLET_TEST_FIXTURE_H

#include <test/test_olivingcoin.h>

#include <interfaces/chain.h>
#include <interfaces/wallet.h>
#include <wallet/wallet.h>

#include <memory>

/** Testing setup and teardown for wallet.
 */
struct WalletTestingSetup: public TestingSetup {
    explicit WalletTestingSetup(const std::string& chainName = CBaseChainParams::MAIN);
    ~WalletTestingSetup();

    std::unique_ptr<interfaces::Chain> m_chain = interfaces::MakeChain();
    CWallet m_wallet;
};

#endif // OLIVINGCOIN_WALLET_TEST_WALLET_TEST_FIXTURE_H
