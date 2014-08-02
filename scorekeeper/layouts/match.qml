import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: match
    width: 480
    height: 272




    function updateScoreA(string ) {
        score_a.text = string
    }

    function updateScoreB(string ) {
        score_b.text = string
    }

    Core.ScoreText {
        id: score_a
        x: 45
        y: 8
        text: qsTr("0")
    }

    Core.ScoreText {
        id: score_b
        x: 303
        y: 8
        text: qsTr("0")
        horizontalAlignment: Text.AlignRight
  
    }

    Core.ScoreText {
        id: dash
        x: 232
        y: 8
        text: qsTr("-")
    }

    

    Core.Button {
        id: a_scored
        x: 45
        y: 218
       
       
        callId: "a_scored"
        btnText: "Score A"
    }

     Core.Button {
        id: b_scored
        x: 307
        y: 218
       
       
        callId: "b_scored"
        btnText: "Score B"
    }

    Core.Button {
        id: end_match
        x: 177
        y: 113
        callId: "end_match"
        btnText: "End Match"
    }

}
