BTCXData = 1:length(BTCData);

figure(1451232);clf;hold on; title 'Prices'
plot(BTCXData, BTCData(:,2)*10^-8);
plot(firstBTC);
plot(secondBTC);
legend('BTC/USD (e-8 corrected)','USD/Coin','USD/Coin');

smoothingFactor = 9;
BTCUSDDiff = diff(smooth(BTCData(:,2), smoothingFactor));
BTCUSDDiff(end + 1) = BTCUSDDiff(end);
cryptoDiff = diff(smooth(firstBTC, smoothingFactor));
cryptoDiff(end + 1) = cryptoDiff(end);

figure(1234123);clf;hold on; title 'Derivatives';
plot(BTCUSDDiff);
plot(cryptoDiff*10^8);
legend('btc/usd','btc/coin (scaled)');

figure(12352135);clf;
scatter(BTCUSDDiff,cryptoDiff);

compEqn = 'a*(x+b)'

cf = fit(cryptoDiff,BTCUSDDiff,compEqn)
figure(1234656363);clf;
plot(cf,cryptoDiff,BTCUSDDiff)
title('curve fit results');
xlabel('BTC/Coin derivative')
ylabel('USD/BTC derivative')
