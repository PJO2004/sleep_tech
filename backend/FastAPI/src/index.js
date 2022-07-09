TESTER = document.getElementById('tester')

Plotly.plot(TESTER,
    [{
        x: ['nia+106@rowan.kr', 'nia+252@rowan.kr', 'nia+067@rowan.kr', 'nia+141@rowan.kr', 'nia+016@rowan.kr', 'nia+188@rowan.kr',
            'nia+279@rowan.kr', 'nia+343@rowan.kr', 'nia+181@rowan.kr', 'nia+118@rowan.kr', 'nia+041@rowan.kr', 'nia+354@rowan.kr',
            'nia+268@rowan.kr', 'nia+438@rowan.kr', 'nia+088@rowan.kr', 'nia+144@rowan.kr',
        ],
        y: [91, 88, 75, 69, 67, 65, 64, 62, 62, 62, 60, 57, 57, 43, 42, 36]
    }], { margin: { t: 10 } }, { showSendToCloud: true });

console.log(Plotly.BUILD)