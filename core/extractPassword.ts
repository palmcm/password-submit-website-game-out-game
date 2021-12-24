import { RoomPasswordMapping } from "../components/PasswordList"
import { encode } from "./encode"
import { wordlist } from "./wordlist"

const getIndexFrom = (encodeRoom:string, start: number, end:number):number => {
    let ans = 0;
    for (let i=start;i<end;i++){
        ans += (i<encodeRoom.length ? encodeRoom[i].charCodeAt(0) : 0)
    }
    return ans;
}

const getWordFrom = (pairs: RoomPasswordMapping[], index: number): string => {
    const {room ,range} = encode[index];
    const con = encode[index].const;
    let ans = 0;
    room.forEach((room:string, ind:number)=>{
        let targetPair = pairs.filter(pair => pair.room == "Room " + room)
        if (targetPair.length < 1) return ans+= con[ind];
        ans+= getIndexFrom(targetPair[0].value, range[ind][0], range[ind][1])*con[ind]
    })
    return wordlist[ans%wordlist.length]
}

const extractPassword = (pairs: RoomPasswordMapping[]): string => {
    let keyPhrase: string = ""
    for (let i=0;i<encode.length;i++){
        keyPhrase += getWordFrom(pairs, i) + " ";
    }

    return keyPhrase.toLowerCase()
}

export default extractPassword