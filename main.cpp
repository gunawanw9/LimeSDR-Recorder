#include "mainwindow.h"
#include <QSplashScreen>
#include <QApplication>
#include <QFile>

void loadModules(QSplashScreen* psplash)
{
    QTime time;
    time.start();

    for (int i = 0; i < 100; ) {
        if (time.elapsed() > 30) {
            time.start();
            ++i;
        }

      psplash->showMessage("Загрузка данных: "
                             + QString::number(i) + "%",
                             Qt::AlignHCenter | Qt::AlignBottom,
                             Qt::white
                            );
    }
}

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QSplashScreen splash(QPixmap("/home/sdr/Qt/Projects/RecordSDRProject/icons/gfyyt.jpg"));
            splash.show();
            loadModules(&splash);
    MainWindow w;
    splash.finish(&w);
    w.show();
    return a.exec();
}
