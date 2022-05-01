# Whims - You Communicate with Melodies
Whims is a social application of ideology, that restricts you only communicate with others by melodies. The ideal of Whims
comes from Herman Hesse's *The Glass Bead Game*, which mentioned how music can be a language of soul and how will you feel
when correctly listening to the music.

Currently the developer is using Flask on Python + JS to develop the prototype of Whims, and is intended to transfer the application
onto an advance framework in the future.

-------

# Whims - 仅用音乐沟通
Whims是一个理念型社交App，仅通过音乐与他人建立联系、进行交流。Whims的理念是“音乐是沟通灵魂的语言”，可参考赫尔曼黑塞的《玻璃球游戏》，其中提及音乐作为一种沟通灵魂的语言，以及聆听正确的音乐的时候应当产生的体验。

## 进度 (Prototype)
- [x] 设计登录/注册功能
- [x] 设计blog CRUD功能
- [ ] 设计基础按键功能
- [ ] 设计基础的base、登录/注册页面（前端）
- [ ] 设计个人主页
  - [ ] 添加Bio
  - [ ] Bio CRUD
- [ ] 设计chat页面
- [ ] 设计discover页面


## 计划开发的功能

### 按键
按键将是Whims中最基础的功能。Whims中的音乐应当使用提供的按键进行编辑，这要求按键具有一定的灵活度，使得其能够表达丰富的旋律。按键应当支持：
#### Start Timer
计时器允许用户开始录制音乐。在用户按下了第一个按键的时候，计时器立刻开始计时，直至用户选择停止。在此之间的按键行为将被完全记录。
#### 更换乐器
为了使得用户能更丰富地演奏音乐，按键应当可以更换乐器
#### 快捷键（？）


### Homepage
Whims的每一个用户将拥有一个Homepage作为登陆后的初始界面。Homepage目前计划包含以下功能：
#### Bio
Bio、账户名字和Blog将是App中能够自由使用文字的全部地方。Bio可以附上个人简介，可以将自己引向外部链接。App剩余的部分仅能使用音乐作为交流方式。
#### Settings
用户可以对个人账号的属性进行丰富的设置，并由此登录/退出账号。

### Blog
Blog的目的是发布和长篇文字一般的抒情音乐，音乐的内容不应是双人沟通的语句，而是一人面向大家的广播。因此，Blog中的音乐与市面上流行的音乐功能相近。
Blog可使用文字设立标题。Blog计划包含以下功能：
#### （理想情况下）编辑音乐按钮的位置
用户可以自由编辑各种按钮的位置，使得按钮以用户希望的图案排列。显示博文的时候，博客界面将显示按钮排列的缩略图/全图。
#### 发布/编辑音乐
当用户编辑音乐的时候，按键只能固定排列。用户可以在完成编辑以后自由更改按键的位置。
#### 浏览主页
用户可以浏览他人的主页。
#### 更改音乐
界面与编辑音乐相同。
#### 删除音乐
将一首博文删除。
#### 浏览音乐
浏览目前的博文的时候，所浏览的内容应当是按键随着音乐而闪烁的按键历史，完美复原用户编辑音乐时候所记录的历史。

### Chat
用户除了可以以音乐作为博文发布以外，还应当可以以短小的音乐语句作为沟通的方式进行聊天，此将是App的核心功能。聊天界面相对Blog，不会提供按键的“可视化”功能，因为对于
聊天而言，按键的功能性要求将会更高。用户将可以：
#### 输入音乐
与编辑博文类似，用户可以在计时器开始以后立刻录制音乐。录制下来的音乐允许被修改，随即发送至对方。
#### 接受音乐
在接受音乐的时候，用户将只能听到音乐的序列，不再能看到可视化的按键排列。这是因为对于聊天而言可视化将阻碍聊天的功能。
#### 群聊？
作者较悲观，不打算设计群聊。

### Discovery
为了方便用户进行社交建立联系，App应设立一个探索面板，以方便用户发现陌生的新用户并产生联系。探索面板具体功能待设计。