data3=[data1;data2];
theclass=ones(400,1);
theclass(1:200)=0;
cl = fitcsvm(data3,theclass,'KernelFunction','rbf',...
    'BoxConstraint',0.1,'KernelScale',0.5,'ClassNames',[0,1]);

d = 0.02;
[x1Grid,x2Grid] = meshgrid(min(data3(:,1)):d:max(data3(:,1)),...
    min(data3(:,2)):d:max(data3(:,2)));
xGrid = [x1Grid(:),x2Grid(:)];
[~,scores] = predict(cl,xGrid);

figure;
h(1:2) = gscatter(data3(:,1),data3(:,2),theclass,'rb','.');
hold on
h(3) = plot(data3(cl.IsSupportVector,1),data3(cl.IsSupportVector,2),'ko');
contour(x1Grid,x2Grid,reshape(scores(:,2),size(x1Grid)),[0 0],'k'); %decision boundary
legend(h,{'0','+1','Support Vectors'});
axis equal
hold off
