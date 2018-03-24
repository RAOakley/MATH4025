cryptoNames = {'STORJ','MAID','SC'};
inUSD = false;
cryptoData = cryptoNames;

%{
firstCoin = csvread(['../', cryptoNames{1}, '_daily.csv']);
secondCoin = csvread(['../', cryptoNames{2}, '_daily.csv']);
thirdCoin = csvread(['../', cryptoNames{3}, '_daily.csv']);
%}

for i=1:length(cryptoNames)
    cryptoData{i} = csvread(['../', cryptoNames{i}, '.csv']);
end

firstCoin = cryptoData{1};
secondCoin = cryptoData{2};
thirdCoin = cryptoData{3};

figure(123234);clf;hold on; title 'Coin Prices'
plot(firstCoin(1,:), firstCoin(2,:));
plot(secondCoin(1,:), secondCoin(2,:));
plot(thirdCoin(1,:), thirdCoin(2,:));
legend({'STORJ','MAID','SC'}, 'Location', 'northwest');


for i = 2:length(secondCoin(2,:))
    secondCoin(5,i) = secondCoin(2,i) - secondCoin(2,i-1);
end
secondCoin(5,:) = sign(secondCoin(5,:));
%Xs = secondCoin(3:5,:);
%Ys = secondCoin(2,:);
Xs = secondCoin(2:3,:);
Ys = secondCoin(5,:);


%{
startPoint = 1000;
firstBTCp = firstCoin(startPoint:end,2);
secondBTCp = secondCoin(startPoint:end,2);

xData = 1:length(firstBTCp);

figure(124355378);clf;hold on; title 'BTC Prices'
plot(xData,firstBTCp);
plot(xData,secondBTCp);
    

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