cryptoNames = {'STORJ','MAID'}; %SC, BTC
inUSD = false;
%cryptoData = {};

BTCData = csvread('BTC.csv');
dataLength = length(BTCData);

firstUSD = csvread([cryptoNames{1}, '.csv']);
secondUSD = csvread([cryptoNames{2}, '.csv']);

figure(123234);clf;hold on; title 'USD Prices'
plot(firstUSD(:,1),firstUSD(:,2));
plot(secondUSD(:,1),secondUSD(:,2));

firstBTC = firstUSD;
secondBTC = secondUSD;
firstBTC(:,2) = firstBTC(:,2) ./ BTCData(:,2);
secondBTC(:,2) = secondBTC(:,2) ./ BTCData(:,2);

firstBTC = firstBTC(1:end,2);
secondBTC = secondBTC(1:end,2);

