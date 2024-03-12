import cv2
import tkinter as tk



def main():
    # 学習済みのモデル（カスケード分類機）を読み込む
    cascade = cv2.CascadeClassifier(entry1)
    # cascade = cv2.CascadeClassifier("C:/OpenCV4.5.4/opencv-master/opencv-master/data/haarcascades_cuda/haarcascade_frontalface_default.xml")
    # cascade = cv2.CascadeClassifier("C:/OpenCV4.5.4/opencv-master/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")

    # 内蔵カメラから画像データを取得
    cap = cv2.VideoCapture(0)

    # 画像の読み込みができているか確認
    if not cap.isOpened():
        print('正常に機能していません')
        exit()

    # カメラから連続的にキャプチャ画像を取得 

    while True:
        ret, frame = cap.read()
    
        if not ret:
            print('画像を読み込めませんでした')
            break
        # グレースケールに変更
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # 顔を検出
        det_face = cascade.detectMultiScale(gray_scale, minSize=(50,50))
    
        # 顔を赤い長方形で囲む
        for (x,y,w,h) in det_face:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), thickness=2)
        
            # 顔認識を行っている画像を表示
            cv2.imshow('video image', frame)
        
            # qが押されたらwhileから抜ける
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
# root.geometry('400 * 100')
root.title('カスケード分類機を使用した顔認証')

label1 = tk.Label(root, text='カスケード分類機の格納場所を指定')
label1.place(x=100,y=50)
entry1 = tk.Entry(root,widh = 5)

button = tk.Button(root,width = 10, text='実行')
main()


root.mainloop()
