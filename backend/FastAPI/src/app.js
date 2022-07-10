const pg = require('pg');

const port = 3000

const client = new pg.Pool({
  host: 'localhost',
  user: 'postgres',
  password: 'postgres',
  database: 'postgres',
  port: 5432
})

client.connect(err => {
  if (err) {
    console.log('Failed to connect db ' + err)
  } else {
    console.log('Connect to db done!')
  }
})

pg.query("select * from processing;",(err, res)=>{
  if(err != null){
    console.log(err);
  }
  // 클라이 언트에서 얻어온 데이터
  res.send({'data':res.rows})
})