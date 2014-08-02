import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: recentmatches
    width: 480
    height: 272

    function updateScoreA(string ) {
        score_a.text = string
    }

    function updateScoreB(string ) {
        score_b.text = string
    }

    function updateTeamA(playerIds){
        teamaplayers.text = playerIds
    }
    
    function updateTeamB(playerIds){
        teambplayers.text = playerIds
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

    Core.PlayerText {
        id: teamaplayers
        x: 10
        y: 127
         text: qsTr("(no player scanned)")
       
    }

    Core.PlayerText {
        id: teambplayers
        x: 256
        y: 127
       
        text: qsTr("(no player scanned)")
        horizontalAlignment: Text.AlignRight
    }

    Core.Button {
        id: back
        x: 177
        y: 113
        callId: "back"
        btnText: "Back"
    }

}
