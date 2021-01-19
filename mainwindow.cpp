#include "mainwindow.h"
#include "ui_mainwindow.h"

static QString main_path = QDir::homePath();
static QString dir_scripts = main_path;
static QString dir_saving = main_path;
static QProcess *process_analyze;
static QProcess *process_saving;
static QString global_command_part1;
static QString global_filename;
static bool active_record = false;
static QString global_freq_rec;
static QString global_samp_rate_rec;
static QProcess *proc_lime;
static int count_records = 0;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    moveToCenter();
    ui->pushButton_5->setEnabled(false);

    if (ui->lineEdit_2->text() != "") {
        dir_scripts = ui->lineEdit_2->text();
        ui->textBrowser->append("Каталог со скриптами выбран:");
        ui->textBrowser->append(ui->lineEdit_2->text());
//        ui->pushButton_4->setEnabled(false);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::closeEvent(QCloseEvent *event)
 {
    QMessageBox::StandardButton resBtn = QMessageBox::question( this, "LimeRecord",
                                                                    tr("Завершить работу?\n"),
                                                                    QMessageBox::Yes | QMessageBox::No,
                                                                    QMessageBox::Yes);
        if (resBtn != QMessageBox::Yes) {
            event->ignore();
        } else {
            event->accept();
        }
 }

void MainWindow::on_pushButton_clicked()
{
    QString dir = QFileDialog::getExistingDirectory(this, tr("Выберите каталог для сохранения записей"),
                                                    main_path,
                                                    QFileDialog::ShowDirsOnly
                                                    | QFileDialog::DontResolveSymlinks);
    if (dir != "") {
        dir_saving = dir;
        ui->textBrowser->append("Каталог для сохранения выбран.");
        ui->lineEdit->setText(dir_saving);
        ui->pushButton->setEnabled(false);
    }
}


void MainWindow::moveToCenter(){
        this->setGeometry(
            QStyle::alignedRect(
                Qt::LeftToRight,
                Qt::AlignCenter,
                this->size(),
                QGuiApplication::screens().first()->geometry()
            )
        );
}

void MainWindow::on_pushButton_4_clicked()
{
    QString dir = QFileDialog::getExistingDirectory(this, tr("Выберите каталог со скриптами"),
                                                    main_path,
                                                    QFileDialog::ShowDirsOnly
                                                    | QFileDialog::DontResolveSymlinks);
    if (dir != "") {
        dir_scripts = dir;
        ui->textBrowser->append("Каталог со скриптами выбран.");
        ui->lineEdit_2->setText(dir_scripts);
        ui->pushButton_4->setEnabled(false);
    }
}

void MainWindow::on_pushButton_3_clicked()
{
    proc_lime = new QProcess(this);
    proc_lime->setProcessChannelMode(QProcess::MergedChannels);
    proc_lime->start("LimeUtil --find");
    proc_lime->waitForFinished(3500);
    QString string_lime_find=proc_lime->readAllStandardOutput();
    qDebug() << string_lime_find;
    proc_lime->close();
    QString errorconnect = "\n";

    if (string_lime_find!=errorconnect) {
    process_analyze = new QProcess(this);
    process_analyze->setProcessChannelMode(QProcess::ForwardedChannels);
    QString file_path_abs = dir_scripts + "/lime_rx_spectrum.py";
    QString command_to_analyze = "python2 -u \"";
    command_to_analyze += file_path_abs;
    QString samp_rate = QString::number(ui->spinBox_setPolosa->value());
    QString freq = QString::number(ui->spinBox_setFreq->value());
    command_to_analyze += "\" -s ";
    command_to_analyze += samp_rate;
    command_to_analyze += " -f ";
    command_to_analyze += freq;
    qDebug() << command_to_analyze;
    process_analyze->start(command_to_analyze);}

    else {
        QMessageBox msgBox;
        msgBox.setText("Подключите SDR");
        msgBox.setIcon(QMessageBox::Warning);
        msgBox.exec();
        ui->textBrowser->append("Приемник LimeSDR не подключен");
    }
}

void MainWindow::on_pushButton_2_clicked()
{
    proc_lime = new QProcess(this);
    proc_lime->setProcessChannelMode(QProcess::MergedChannels);
    proc_lime->start("LimeUtil --find");
    proc_lime->waitForFinished(3500);
    QString string_lime_find=proc_lime->readAllStandardOutput();
    qDebug() << string_lime_find;
    proc_lime->close();
    QString errorconnect = "\n";

    if (string_lime_find!=errorconnect) {

        ui->textBrowser->clear();

        if (dir_scripts == main_path){
            ui->textBrowser->append("Каталог для скриптов - по умолчанию (главный)");
        }
        if (dir_saving == main_path){
            ui->textBrowser->append("Каталог для сохранения - по умолчанию (главный)");
        }
        ui->pushButton_4->setEnabled(false);
        ui->pushButton->setEnabled(false);
        process_saving = new QProcess(this);
        process_saving->setProcessChannelMode(QProcess::ForwardedChannels);
        QString file_path_abs = dir_scripts + "/lime_rx_save.py";
        global_command_part1 = "python2 -u \"";
        global_command_part1 += file_path_abs;

        global_samp_rate_rec = QString::number(ui->spinBox_setPolosa_2->value());
        global_freq_rec = QString::number(ui->spinBox_setFreq_2->value());

        global_command_part1 += "\" -s ";
        global_command_part1 += global_samp_rate_rec;
        global_command_part1 += " -f ";
        global_command_part1 += global_freq_rec;
        global_command_part1 += " -p ";

        global_filename = dir_saving + "/rec_";
        QString CurrentDateTime = GetCurrentDateTime();
        global_filename += CurrentDateTime;
        global_filename += "_freq_" + global_freq_rec + "_short.bin";

        QString common_command = global_command_part1 + "\"" + global_filename + "\"";
        qDebug() << global_filename;
        count_records = count_records + 1;
        process_saving->start(common_command);
        active_record = true;
        startSizeMonitoring();
        ui->pushButton_2->setEnabled(false);
        ui->pushButton_5->setEnabled(true);}

    else {
        QMessageBox msgBox;
        msgBox.setText("Подключите SDR");
        msgBox.setIcon(QMessageBox::Warning);
        msgBox.exec();
        ui->textBrowser->append("Приемник LimeSDR не подключен");
    }
}

void MainWindow::startSizeMonitoring(){
    timer = new QTimer();
    connect(timer, SIGNAL(timeout()), this, SLOT(slotTimerAlarm()));
    timer->start(5000);
}

void MainWindow::slotTimerAlarm() {

    qint64 fsize = getFileSize(global_filename);
    qint64 max_size = (ui->spinBox->value()) * 1000000000;

    if (fsize > max_size) {
       if (active_record == true) {
           process_saving->kill();
           process_saving->close();
           ui->textBrowser->append("ok[" + QString::number(count_records) + "]" + ": " + global_filename);
           active_record = false;

           global_filename = dir_saving + "/rec_";
           QString CurrentDateTime = GetCurrentDateTime();
           global_filename += CurrentDateTime;
           global_filename += "_freq_" + global_freq_rec + "_short.bin";

           QString common_command = global_command_part1 + "\"" + global_filename + "\"";
           qDebug() << global_filename;

           process_saving->start(common_command);
           active_record = true;
           count_records = count_records + 1;
       }


    }

}


QString MainWindow::fileSize(qint64 nSize)
{
    qint64 i = 0;
    for (; nSize > 1023; nSize /= 1024, ++i) { }
    return QString().setNum(nSize) + "BKMGT"[i];
}

QString MainWindow::GetCurrentDateTime() {
    QDateTime currDTime = QDateTime::currentDateTime();
    QString currDT = currDTime.toString("hh.mm.ss_dd.MM.yy");
    return currDT;
}

qint64 MainWindow::getFileSize(const QString &path)
{
    qint64 size = 0;
    QFileInfo fileInfo(path);

    if(fileInfo.isSymLink() && fileInfo.size() == QFileInfo(fileInfo.symLinkTarget()).size())
    {
        // Try this approach first
        QFile file(path);
        if(file.exists() && file.open(QIODevice::ReadOnly))
            size = file.size();
        file.close();

        // If that didn't work, try this
        if(size == 0)
        {
            QString tmpPath = path+".tmp";
            for(int i=2; QFileInfo().exists(tmpPath); ++i) // Make sure filename is unique
                tmpPath = path+".tmp"+QString::number(i);

            if(QFile::copy(path, tmpPath))
            {
                size = QFileInfo(tmpPath).size();
                QFile::remove(tmpPath);
            }
        }
    }
    else size = fileInfo.size();

    return size;
}

void MainWindow::on_pushButton_5_clicked()
{
    process_saving->terminate();
    ui->pushButton_5->setEnabled(false);
    ui->pushButton_2->setEnabled(true);
    ui->textBrowser->append(" ");
    ui->textBrowser->append("Запись остановлена.");
    ui->textBrowser->append("Всего: " + QString::number(count_records));

}
