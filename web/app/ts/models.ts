/// <reference path='../_all.ts' />

module app {
    'use strict'
    

    export class Entry
    {
        data: any;
        head: string
        time: Date;
        counterpart: string;
        constructor (entry: string){
            var tmp = entry.replace(/ - \d/g,"   ").split(" - ");
            this.time = new Date(tmp[0].split(",")[0]);
            var pos = tmp[1].search("{");
            this.counterpart  = tmp[1].substr(0,pos);
            var obj = JSON.parse((tmp[1].substr(pos,tmp[1].length)).replace(/u'/g,"'").replace(/'/g,'"'));
            this.data = obj.data;
            this.head = obj.head;
        }

    }

    export interface Session {
        uid: string;
        decuid: string;
        entries: Array<Entry>; 
        duration:  number;
        type: string; 
    }
  

    export class Log {
     
        entries: Array<string>;
        sessions: Array<Session>;
        uids: Array<string>;
        constructor(log: string) {
            this.entries = log.split("\n");

        }

        getEntries()
        {
            return this.entries;
        }

        getSessions()
        {
            this.sessions = [];
            this.uids = []
            var current: Session = {type:"", duration:0,decuid: "", uid: "", entries: []}

            this.entries.forEach(e => {


                if(e.search ("2014-07-10") != -1 || e.search ("2014-07-11") != -1 || e.search ("2014-07-12") != -1)
                {
                    
                if (e.search("common/balanceScan") != -1)
                {
                    current.type += "Balance";
                }
                  

                    var pos = e.search("u'tag', u'data': u'")
                    if ( pos != -1)
                    {
    
                        current.uid += e.substr(pos + 19, 8);
                        current.decuid = parseInt(current.uid, 16).toString(10);
                        this.uids.push(current.uid);     
                    } 
                    if ( e.search("finished") != -1)
                    {
                        this.sessions.push(current)
                    
                        current.duration = current.entries[current.entries.length - 1].time.getTime() - current.entries[0].time.getTime() ;
    
                        current = {type:"",duration:0, decuid: "",uid: "", entries: []}
                    } else {
                        try
                        {
                            current.entries.push(new Entry(e));
                        } 
                        catch(Error){
                            window.console.log(Error + e);
                        }
                    }
                }
            });
            return this.sessions;
        }
    }

}
