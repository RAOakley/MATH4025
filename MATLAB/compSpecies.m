smoothingFactor = 9;
derivatives = diff(smooth(firstBTC, smoothingFactor));
derivatives(end + 1) = derivatives(end);
figure(1242341);clf;hold on
plot(derivatives);
plot(firstBTC);
plot(smooth(firstBTC, smoothingFactor));
title 'derivatives after smoothing'
legend('derivative','unsmoothed price','smoothed price (used for derivative)');

compEqn = 'a*x*(1-(x + b*y)/c)'

cf = fit([firstBTC, secondBTC],derivatives,compEqn)
figure(1241234512);clf;
plot(cf,[firstBTC, secondBTC],derivatives)
title('curve fit results');
xlabel('first coin')
ylabel('second coin')
zlabel('first coin R.o.C');