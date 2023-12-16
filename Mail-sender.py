import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        self.kullanici_adi = ""
        self.parola = ""
        Form.setObjectName("Form")
        Form.resize(769, 336)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.kullanici_adi_giris = QtWidgets.QPlainTextEdit(Form)
        self.kullanici_adi_giris.setObjectName("kullanici_adi_giris")
        self.gridLayout_2.addWidget(self.kullanici_adi_giris, 0, 1, 1, 1)
        self.giris_buton = QtWidgets.QPushButton(Form)
        self.giris_buton.setObjectName("giris_buton")
        self.gridLayout_2.addWidget(self.giris_buton, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.parola_giris = QtWidgets.QPlainTextEdit(Form)
        self.parola_giris.setPlainText("")
        self.parola_giris.setObjectName("parola_giris")
        self.gridLayout_2.addWidget(self.parola_giris, 1, 1, 1, 1)
        self.onay_metni = QtWidgets.QPlainTextEdit(Form)
        self.onay_metni.setObjectName("onay_metni")
        self.gridLayout_2.addWidget(self.onay_metni, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gnderilecek_kisi_yazi = QtWidgets.QPlainTextEdit(Form)
        self.gnderilecek_kisi_yazi.setPlainText("")
        self.gnderilecek_kisi_yazi.setObjectName("gnderilecek_kisi_yazi")
        self.gridLayout.addWidget(self.gnderilecek_kisi_yazi, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.gonder = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gonder.setFont(font)
        self.gonder.setObjectName("gonder")
        self.gridLayout.addWidget(self.gonder, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.konu_yazi = QtWidgets.QPlainTextEdit(Form)
        self.konu_yazi.setPlainText("")
        self.konu_yazi.setObjectName("konu_yazi")
        self.gridLayout.addWidget(self.konu_yazi, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.metin_yazi = QtWidgets.QPlainTextEdit(Form)
        self.metin_yazi.setPlainText("")
        self.metin_yazi.setObjectName("metin_yazi")
        self.gridLayout.addWidget(self.metin_yazi, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.giris_buton.clicked.connect(self.mail_giris)
        self.gonder.clicked.connect(self.mail_gonder)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.giris_buton.setText(_translate("Form", "Mail\'e Giriş Yap"))
        self.label_4.setText(_translate("Form", "Parola:"))
        self.label_5.setText(_translate("Form", "Kullanıcı Adı:"))
        self.gonder.setText(_translate("Form", "Gönder!"))
        self.label.setText(_translate("Form", "Mail\'in Konusu:"))
        self.label_2.setText(_translate("Form", "Gönderilecek Mail Metni:"))
        self.label_3.setText(_translate("Form", "Gönderilecek kişinin mail adresi:"))

    def mail_giris(self):
        self.kullanici_adi = self.kullanici_adi_giris.toPlainText()
        self.parola = self.parola_giris.toPlainText()
        if (self.kullanici_adi == "x@gmail.com" and self.parola == "x"):
            self.onay_metni.setPlainText("Başarıyla Giriş Yapıldı.")
        else:
            self.onay_metni.setPlainText("Kullanıcı Adı Veya Parola Hatalı.")

    def mail_gonder(self):
        mesaj = MIMEMultipart()
        mesaj["From"] = self.kullanici_adi
        mesaj["To"] = self.gnderilecek_kisi_yazi.toPlainText()
        mesaj["Subject"] = self.konu_yazi.toPlainText()

        yazi = self.metin_yazi.toPlainText()

        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.kullanici_adi, self.parola)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            self.onay_metni.setPlainText("E-Posta Gönderildi.")
            mail.close()
        except smtplib.SMTPAuthenticationError:
            self.onay_metni.setPlainText("Hata: SMTP kimlik doğrulama hatası. Kullanıcı adı veya parola hatalı.")

        except smtplib.SMTPConnectError:
            self.onay_metni.setPlainText("Hata: SMTP bağlantı hatası. Bağlantı kurulamadı.")

        except smtplib.SMTPException as e:
            self.onay_metni.setPlainText(f"Hata: {e}")

        except Exception as e:
            self.onay_metni.setPlainText(f"Bilinmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())