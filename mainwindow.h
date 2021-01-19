#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMainWindow>
#include <QMainWindow>
#include <QProcess>
#include <QMessageBox>
#include <QFileDialog>
#include <QFile>
#include <QTimer>
#include <QTime>
#include <QDebug>
#include <QDesktopWidget>
#include <QStatusBar>
#include <QCloseEvent>
#include <QScreen>
#include <QStyle>
#include <QThread>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void moveToCenter();
     void closeEvent(QCloseEvent *event);
    void startSizeMonitoring();
    QString fileSize(qint64 nSize);
    qint64 getFileSize(const QString &path);
    QString GetCurrentDateTime();

private slots:
    void on_pushButton_clicked();
    void on_pushButton_4_clicked();
    void on_pushButton_3_clicked();
    void on_pushButton_2_clicked();
    void slotTimerAlarm();
    void on_pushButton_5_clicked();

private:
    Ui::MainWindow *ui;

    QTimer *timer;
};
#endif // MAINWINDOW_H
