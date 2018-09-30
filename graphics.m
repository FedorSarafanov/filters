load('filters')
C=0.025*10^-6;
L=8.5*10^-3;
R=583;
set(0,'defaultTextInterpreter','latex');

h = figure;
u=filters1.u/max(filters1.u);
plot(filters1.f,u,'r*')
ylabel('$A(\nu)$','FontSize',18)
xlabel('$\nu, Hz$','FontSize',18)
grid on
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
print(h,'graph\graph1','-dpdf','-r0')
h=figure();
plot(filters1.f,filters1.p,'b*')
ylabel('$\Phi(\nu)$','FontSize',18);
xlabel('$\nu, Hz$','FontSize',18);
grid on
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
print(h,'graph\graph2','-dpdf','-r0')





h = figure;
u=filters2.u/max(filters2.u);
plot(filters2.f,u,'r*')
ylabel('$A(\nu)$','FontSize',18)
xlabel('$\nu, Hz$','FontSize',18)
grid on
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
print(h,'graph\graph3','-dpdf','-r0')
h=figure();
plot(filters2.f,filters2.p,'b*')
ylabel('$\Phi(\nu)$','FontSize',18);
xlabel('$\nu, Hz$','FontSize',18);
grid on
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
print(h,'graph\graph4','-dpdf','-r0')




h = figure;
u=filters3.u/max(filters3.u);
plot(filters3.f,u,'r*')
ylabel('$A(\nu)$','FontSize',18)
xlabel('$\nu, Hz$','FontSize',18)
grid on
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
print(h,'graph\graph5','-dpdf','-r0')
h=figure();
plot(filters3.f,filters3.p,'b*')
ylabel('$\Phi(\nu)$','FontSize',18);
xlabel('$\nu, Hz$','FontSize',18);
grid on
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
print(h,'graph\graph6','-dpdf','-r0')
