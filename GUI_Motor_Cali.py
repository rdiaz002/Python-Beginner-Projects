import tkinter as tk
import threading
#import RPi.GPIO as GPIO 
current_state=0;
pin=0;
frequency=0;
dutycycle=0;
 

def state_machine():
    GPIO.setmode(GPIO.BOARD);
    global current_state , pin , frequency , dutycycle 
    GPIO.setup(pin,GPIO.OUT);
    d=GPIO.PWM(pin,frequency);
    d.start(dutycycle);
    current_state=1;
    try:
        while(current_state!=6):
            
            if(current_state==2):
                d.ChangeDutyCycle(dutycycle);
                print("dutycycle:",dutycycle);
                current_state=1;
            elif(current_state==3):
                d.ChangeFrequency(frequency);
                print("frequency:",frequency);
                current_state=1;
            elif(current_state==4):
                d.stop();
                GPIO.cleanup();
                current_state=6;
            else:
                pass;
        print("exit success");
    except:
        print("there was a problem")
        d.stop();
        GPIO.cleanup();

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=10,column=10);
        global current_state , pin , frequency , dutycycle
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self , text ="Frequency",command = self.change_freq);
        self.hi_there.grid(column = 1 ,row = 0,padx=5,pady=5);
        self.text_here=tk.Text(self,height=1,width=20);
        self.text_here.grid(column=0,row=0,padx=5,pady=5);
        self.DutyCycle = tk.Button(self , text ="DutyCycle",command = self.change_duty);
        self.DutyCycle.grid(column = 1 ,row = 1,padx=5,pady=5);
        self.DutyText=tk.Text(self,height=1,width=20);
        self.DutyText.grid(column=0,row=1,padx=5,pady=5);
        self.Startup = tk.Button(self, text = "Turn On",command = self.start_thread );
        self.Startup.grid(column=5,row=5,padx =5);
        self.label2 = tk.Label(self,text="freq");
        self.label2.grid(column=4,row=4,padx =1);
        self.label1 = tk.Label(self,text="duty");
        self.label1.grid(column=4,row=3,padx =1);
        self.label3 = tk.Label(self,text="pin");
        self.label3.grid(column=4,row=2,padx =1);
        
        self.up_freq = tk.Text(self,height = 1, width =4);
        self.up_freq.grid(column=5,row=4);
        self.up_duty = tk.Text(self,height = 1, width =4);
        self.up_duty.grid(column=5,row=3);
        self.pin_local = tk.Text(self,height = 1, width =2);
        self.pin_local.grid(column=5,row=2);
        self.shutoff = tk.Button(self,text="ShutDown",command = self.exit);
        self.shutoff.grid(column=5,row=6,padx =5);
        self.label4 = tk.Label(self,text="Frequency").grid(column=0,row=6);
        self.label4 = tk.Label(self,text="DutyCycle").grid(column=2,row=6);
        self.up_butt = tk.Button(self,text="UP",command=self.increase_freq);
        self.up_butt.grid(column=0,row=7,pady=10);
        self.down_butt = tk.Button(self,text="DOWN",command=self.decrease_freq);
        self.down_butt.grid(column=0,row=9,pady=10);
        self.up_butt = tk.Button(self,text="UP",command=self.increase_duty);
        self.up_butt.grid(column=2,row=7,pady=10);
        self.down_butt = tk.Button(self,text="DOWN",command=self.decrease_duty);
        self.down_butt.grid(column=2,row=9,pady=10);
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(column=5,row=10,padx=0);

    def start_thread(self):
        global pin , frequency , dutycycle
        pin=int(self.pin_local.get("1.0",tk.END));
        frequency=int(self.up_freq.get("1.0",tk.END));
        dutycycle=int(self.up_duty.get("1.0",tk.END));
        self.t=threading.Thread(target = state_machine);
        self.t.start();
    def change_freq(self):
        global current_state , frequency
        frequency=int(self.text_here.get("1.0",tk.END));
        current_state=3;
    def change_duty(self):
        global current_state , dutycycle
        dutycycle=int(self.DutyText.get("1.0",tk.END));
        current_state=2;
    def increase_freq(self):
        global current_state , frequency
        frequency+=10;
        current_state=3;
    def increase_duty(self):
        global current_state , dutycycle
        dutycycle+=1;
        current_state=2;
    def decrease_freq(self):
        global current_state , frequency
        frequency-=10;
        current_state=3;
    def decrease_duty(self):
        global current_state , dutycycle
        dutycycle-=1;
        current_state=2;
    def exit(self):
        global current_state
        current_state=4;
        self.t.join();
        

root = tk.Tk()
root.wm_title("ESC control and Calibration");
app = Application(master=root)
app.mainloop()

