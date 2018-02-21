cryptoNames = {'STORJ','MAID'}; %SC, BTC
inUSD = false;
%cryptoData = {};

BTCData = csvread('../BTC.csv');
dataLength = length(BTCData);

firstUSD = csvread(['../', cryptoNames{1}, '.csv']);
secondUSD = csvread(['../', cryptoNames{2}, '.csv']);

figure(123234);clf;hold on; title 'USD Prices'
plot(firstUSD(:,1),firstUSD(:,2));
plot(secondUSD(:,1),secondUSD(:,2));

firstBTC = firstUSD;
secondBTC = secondUSD;
firstBTC(:,2) = firstBTC(:,2) ./ BTCData(:,2);

secondBTC(:,2) = secondBTC(:,2) ./ BTCData(:,2);

for i = 2:length(BTCData(:,2))
    secondBTC(i,3) = secondBTC(i,2) - secondBTC(i-1,2);
end
secondBTC(:,4) = sign(secondBTC(:,3));
Xs = secondBTC(611:end,2);
Ys = secondBTC(611:end,4);

startPoint = 1000;
firstBTCp = firstBTC(startPoint:end,2);
secondBTCp = secondBTC(startPoint:end,2);

xData = 1:length(firstBTCp);

figure(124355378);clf;hold on; title 'BTC Prices'
plot(xData,firstBTCp);
plot(xData,secondBTCp);


    
%{
figure(12341234);clf;hold on;
for i = 1:length(cryptoNames)
    figure(i);clf;
    figure(12341234);
    fileName = [cryptoNames{i}, '.csv'];
    cryptoData{i} = csvread(fileName)';
    maxLength = max(maxLength, length(cryptoData{i}));
    plot(cryptoData{i}(2,:))
    title([cryptoNames(i), ' price vs. time']);
end

for i = 1:length(cryptoNames)
    cryptoData{i}(1,:) = cryptoData{i}(1,:) + maxLength - max(cryptoData{i}(1,:));
    plot(cryptoData{i}(1,:),cryptoData{i}(2,:));
end

%}