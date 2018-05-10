Public Class Form1
    Private Sub OpenFileDialog2_FileOk(sender As Object, e As System.ComponentModel.CancelEventArgs)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Shell("cmd.exe /k" + "netsh advfirewall firewall add rule name='UplayOfflineMode' dir=out action=block program='%ProgramFiles% (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe' enable=no")
        ' Shell("cmd.exe /k" + "echo kwai all")
    End Sub
End Class